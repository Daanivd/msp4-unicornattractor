from django.test import TestCase
from django.contrib.auth.models import User

class TestAccountsBackend(TestCase):
    
    def test_authenticate_user_by_email(self):
        user = User.objects.create_user(username='test_user', email='test@test.com',password='password')
        page = self.client.post("/accounts/login/", { 
                                                        'username':'test@test.com',
                                                        'password':'password',
                                                        }, 
                                                        follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
        
    