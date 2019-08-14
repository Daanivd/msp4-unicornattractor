from django.test import TestCase
from .models import OrderLineItem, Order
from django.contrib.auth.models import User
from features.models import Feature

class TestCheckoutModel(TestCase):
    def test_OrderLineItem_as_a_string(self):
            user = User.objects.create_user(username='test_user', password='password')
            feature = Feature(featureName="Test Feature", price=500, author=user)
            orderlineitem = OrderLineItem(user=user, product = feature, contribution='50')
            self.assertEqual("50 Test Feature @ 500", str(orderlineitem))
            
            
    def test_Order_as_a_string(self):
        user = User.objects.create_user(username='test_user', password='password')
        order = Order(
                      full_name = 'name',
                      phone_number = '1234',
                      country = 'country',
                      postcode = '1234',
                      town_or_city = 'town',
                      street_address1 = 'address lane 1',
                      street_address2 = 'app2',
                      province = 'province',
                      )
        order.id='1'
        order.date='2019-08-07'
        order.save()
        self.assertEqual("Order 1-2019-08-07-name", str(order))              
                      
                     
        
            
 