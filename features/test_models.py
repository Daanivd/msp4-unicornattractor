from django.test import TestCase
from .models import Feature
from django.contrib.auth.models import User

class TestFeatureModel(TestCase):
    def test_status_defaults_to_open(self):
        user = User.objects.create_user(username='test_user', password='password')
        feature = Feature(featureName='Test Feature', author=user)
        feature.save()
        self.assertEqual(feature.featureName, 'Test Feature')
        self.assertEqual(feature.status, 1)
    
    def test_feature_as_a_string(self):
            feature = Feature(featureName='Test Feature')
            self.assertEqual('Test Feature', str(feature))
