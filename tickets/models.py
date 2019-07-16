from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Ticket(models.Model):
    """ Status categories of Ticket """
    STATUS = (
            ('1', 'Open'),
            ('2', 'Working on it'),
            ('3','Bug resolved')
            )
    
    """ A ticket """
    ticketName = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    content = models.TextField()
    image = models.ImageField(upload_to="img", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS, default=1)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.ticketName
