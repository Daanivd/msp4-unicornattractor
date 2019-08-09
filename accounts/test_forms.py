from django.test import TestCase
from .forms import LoginForm, UserRegoForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 

# Create your tests here.
class TestRegoForm(TestCase):
    
    def test_email_address_is_unique_true(self):
        User.objects.create_user(email='email@email.com', username='test_username', password='password')
        form = UserRegoForm({'username': 'test_username2','password1': 'password', 'password2': 'password', 'email':'email@email.com'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'Email address must be unique'])
    
    def test_create_account_with_only_a_username(self):
        form = UserRegoForm({'username': 'test_username'})
        self.assertFalse(form.is_valid()) #Passes
        
    def test_create_account_with_no_username(self):
        form = UserRegoForm({'password1': 'password', 'password2': 'password'})
        self.assertFalse(form.is_valid())    
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        
    def test_create_account_with_no_password2(self):
        form = UserRegoForm({'username': 'test_username','password1': 'password'})
        self.assertFalse(form.is_valid())   
        self.assertEqual(form.errors['password2'], [u'This field is required.'])
        
    def test_create_account_with_no_password1(self):
        form = UserRegoForm({'username': 'test_username','password2': 'password'})
        self.assertFalse(form.is_valid())  
        self.assertEqual(form.errors['password2'], [u'Please confirm your password'])    
        
    def test_passwords_dont_match(self):
        form = UserRegoForm({'username': 'test_username','password1': 'Xpassword', 'password2': 'password'})
        self.assertFalse(form.is_valid())  
        self.assertEqual(form.errors['password2'], [u'Passwords must match'])   
        

          
        
       
        
        
        
        