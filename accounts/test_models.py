from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Profile
from django.contrib.auth.models import User


class TestProfileModel(TestCase):

    def test_profile_as_a_string(self):
                user = User.objects.create_user(username='test_user', password='password')
                user.save()
                profile = get_object_or_404(Profile, user=user.id)
                self.assertEqual(str(profile), 'Profile for user test_user')