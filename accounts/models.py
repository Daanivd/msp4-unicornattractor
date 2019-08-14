from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """ Model to add more information to a user """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.TextField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to='img', blank=True, null=True)
    
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
        

"""To create the profile instance for a new user"""        
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()        