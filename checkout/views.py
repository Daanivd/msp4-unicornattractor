from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from features.models import Feature
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    """Get cart-items and proceed to checkout and pay using Stripe"""
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            """Get cart items and save order_line_item"""
            cart = request.session.get('cart', {})
            total = 0
            for id, contribution in cart.items():
                product = get_object_or_404(Feature, pk=id)
                total += int(contribution)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    contribution = contribution,
                    user = request.user
                )
                order_line_item.save()
            
            """Payment through Stripe"""
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency='EUR',
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            
                if customer.paid:
                    messages.error(request, 'Thank you for your contribution')
                    for id, contribution in cart.items():
                        """Add paid amount per item in cart to corresponding feature.totalContributions"""
                        feature = get_object_or_404(Feature, pk=id)
                        # print(feature.totalContributions)
                        feature.totalContributions += int(contribution)
                        feature.save
                        # print(feature.totalContributions)
                        
                    request.session['cart'] = {}    
                        
                    return redirect(reverse('all_features'))
                else:
                    messages.error(request, 'Unable to take payment')
                    
            except stripe.error.CardError:
                messages.error(request, 'Your card was declined!')      
                
        else:
            print(payment_form.errors)
            messages.error(request, 'We were unable to take a payment with that card!')
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, 'checkout.html', {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})