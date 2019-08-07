from django.test import TestCase
from .models import Feature
from django.contrib.auth.models import User
from django.contrib import messages


class TestViews(TestCase):

    def test_get_all_features_page(self):
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")
        
    def test_feature_detail(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        feature = Feature(featureName="Test Feature", author=user)
        feature.save()
        page = self.client.get("/features/{0}".format(feature.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "feature.html")
        
    
    def test_post_request_feature(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        page = self.client.post("/features/", { 
                                                        'description':'test content',
                                                        'featureName': 'test feature',
                                                    }, 
                                                        follow=True)
                                   
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")                                                
        
        
    
  