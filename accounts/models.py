from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.TextField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)