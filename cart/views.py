from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

@login_required
def add_to_cart(request, id):
    """Add a contribution to the feature to the cart"""
    contribution = int(request.POST.get('contribution'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + contribution      
    else:
        cart[id] = cart.get(id, contribution) 
  
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

@login_required
def adjust_cart(request, id):
    """
    Adjust the contribution of the specified feature to the specified
    amount
    """
    contribution = request.POST.get('contribution')
    if contribution:
        contribution = int(contribution)
        
    else:
        contribution = 0
    cart = request.session.get('cart', {})

    if contribution > 0:
            cart[id] = contribution
        
    else:
            cart.pop(id)
    
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))