from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Feature(models.Model):
    STATUS = (
            ('1', 'Open'),
            ('2', 'Awaiting pricing'),
            ('3', 'In development'),
            ('4','Feature added'),
            ('5', 'Closed')
            )
    
    featureName = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS)
    

    def __str__(self):
        return self.featureName