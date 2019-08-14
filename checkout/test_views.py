from django.test import TestCase
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.contrib.auth.models import User
from features.models import Feature
from cart.contexts import cart_contents
from django.contrib import messages


class TestViews(TestCase):
    
    def test_checkout_correct_creditcard_details(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        feature = Feature(featureName='Test Feature', author=user)
        feature.save()
        page = self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': 10}, follow=True)
        stripe_id = 'tok_visa'
        page = self.client.post('/checkout/', {'full_name':'name',
                                               'phone_number':'1234', 
                                               'street_address1':'my', 
                                               'street_address2':'address', 
                                               'town_or_city':'xx', 'province':'ireland', 
                                               'country':'ireland','postcode':'eircode', 
                                               'credit_card_number': '4242424242424242',
                                               'cvv':'111', 'expiry_month':'2',
                                               'expiry_year':'2020', 
                                               'stripe_id':stripe_id}, 
                                               follow=True)
        
        messages = list(page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Thank you for your contribution')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('features.html')
        
        
    def test_checkout_chargeDeclined(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        feature = Feature(featureName='Test Feature', author=user)
        feature.save()
        page = self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': 10}, follow=True)
        stripe_id = 'tok_chargeDeclined'
        page = self.client.post('/checkout/', {'full_name':'name',
                                               'phone_number':'1234', 
                                               'street_address1':'my', 
                                               'street_address2':'address', 
                                               'town_or_city':'xx', 'province':'ireland', 
                                               'country':'ireland','postcode':'eircode', 
                                               'credit_card_number': '4000400040004000',
                                               'cvv':'111', 'expiry_month':'2',
                                               'expiry_year':'2020', 
                                               'stripe_id':stripe_id}, 
                                               follow=True)
        
        messages = list(page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your card was declined!')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('features.html')
        
        
    def test_checkout_invalidForm(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        feature = Feature(featureName='Test Feature', author=user)
        feature.save()
        page = self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': 10}, follow=True)
        stripe_id = 'tok_chargeDeclined'
        page = self.client.post('/checkout/', {'phone_number':'1234', 
                                               'street_address1':'my', 
                                               'street_address2':'address', 
                                               'town_or_city':'xx', 'province':'ireland', 
                                               'country':'ireland','postcode':'eircode', 
                                               'credit_card_number': '4000400040004000',
                                               'cvv':'111', 'expiry_month':'2',
                                               'expiry_year':'2020', 
                                               'stripe_id':stripe_id}, 
                                               follow=True)
        
        messages = list(page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'We were unable to take a payment with that card!')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('features.html')    
   
    def test_get_payment_and_order_form(self):
        user = User.objects.create_user(username='test_user', email='test@test.com', password='password')
        self.client.login(username='test_user', password='password')
        page = self.client.get('/checkout/', follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'checkout.html') 