from django.test import TestCase
from .contexts import cart_contents
from features.models import Feature
from django.contrib.auth.models import User


from django.test import Client

class TestViews(TestCase):

    def test_view_cart(self):
            user = User.objects.create_user(username='test_user', password='password')
            login = self.client.login(username='test_user', password='password')
            self.assertTrue(login)
            page = self.client.get("/cart/")
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, "cart.html")
            
    def test_add_to_cart(self):
        user = User.objects.create_user(username='test_user', password='password')
        login = self.client.login(username='test_user', password='password')
        self.assertTrue(login)
        
        feature = Feature(featureName="Test Feature", author=user)
        feature.save()
        page = self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': 100}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')
        
    def test_add_to_cart_when_not_logged_in(self):
        user = User.objects.create_user(username='test_user', password='password')
        feature = Feature(featureName="Test Feature", author=user)
        feature.save()
        page = self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': 100}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')    
        
    def test_add_to_cart_feature_already_in_cart(self):
        user = User.objects.create_user(username='test_user', password='password')
        login = self.client.login(username='test_user', password='password')
        self.assertTrue(login)
        feature = Feature(featureName="Test Feature", author=user)
        feature.save()
        page = self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': 100}, follow=True)
        page = self.client.post('/cart/add/{0}'.format(feature.id), {'contribution': 200}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')    
        
    def test_adjust_cart(self):
        user = User.objects.create_user(username='test_user', password='password')
        login = self.client.login(username='test_user', password='password')
        self.assertTrue(login)
        feature = Feature(featureName="Test Feature", author=user)
        feature.save()
        page = self.client.post('/cart/adjust/{0}'.format(feature.id), {'contribution': 100}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')    
        
    def test_adjust_cart_when_contribution_is_zero(self):
        user = User.objects.create_user(username='test_user', password='password')
        login = self.client.login(username='test_user', password='password')
        self.assertTrue(login)
        feature = Feature(featureName="Test Feature", author=user)
        feature.save()
        page = self.client.post('/cart/adjust/{0}'.format(feature.id), {'contribution': 100}, follow=True)
        page = self.client.post('/cart/adjust/{0}'.format(feature.id), {'contribution': 0}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')        
        
     