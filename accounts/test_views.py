from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib import messages


class TestViews(TestCase):
    
    def test_registration_new_user(self):
        page = self.client.post("/accounts/registration/", { 
                                                        'username':'test_user',
                                                        'email': 'test@test.com',
                                                        'password1':'password',
                                                        'password2':'password'
                                                    }, 
                                                        follow=True)
        messages = list(page.context['messages'])  
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You have successfully registered with UPS')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
        

    def test_registration_when_user_is_already_authenticated(self):
        user = User.objects.create_user(username='test_user', email='test@test.com',password='password')
        self.client.login(username='test_user', password='password')
        page = self.client.get("/accounts/registration/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_get_registration_form(self):
        page = self.client.get("/accounts/registration/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")    
        
    def test_get_login_form(self):
        page = self.client.get("/accounts/login/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")     
            
    def test_login_user(self):
        user = User.objects.create_user(username='test_user', password='password')
        page = self.client.post("/accounts/login/", { 
                                                        'username':'test_user',
                                                        'password':'password',
                                                        }, 
                                                        follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_login_user_when_already_logged_in(self):    
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        page = self.client.get("/accounts/login/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_login_error(self):
        user = User.objects.create_user(username='test_user', password='password')
        page = self.client.post("/accounts/login/", { 
                                                        'username':'test_user',
                                                        'password':'wrongpassword',
                                                        }, 
                                                        follow=True)
        # messages = list(page.context['messages'])
        # self.assertEqual(len(messages), 1)
        # self.assertEqual(str(messages[0]), 'Your username or password is incorrect')                                                
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")                                                
        
        
    def test_logout_user(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        page = self.client.get("/accounts/logout/", follow=True)
        messages = list(page.context['messages'])  
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You have successfully been logged out')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_user_profile(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        page = self.client.get("/accounts/profile/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
        
        
        
                
            