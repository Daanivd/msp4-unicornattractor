from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Feature(models.Model):
    STATUS = (
            ('1', 'Awaiting pricing'),
            ('2', 'Price set'),
            ('3', 'In development'),
            ('4','Feature added'),
            )
    
    featureName = models.CharField(max_length=254)
    description = models.TextField()
    contribution = models.IntegerField(blank=True, null=True)
    totalContributions = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    set_price_date = models.DateTimeField(blank=True, null=True)
    in_development_date = models.DateTimeField(blank=True, null=True)
    feature_added_date = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    views = models.IntegerField(default=0)
    devComments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS, default=1)
    

    def __str__(self):
        return self.featureName