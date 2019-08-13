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
    description = models.TextField()
    image = models.ImageField(upload_to="img", blank=True, null=True)
    published_date = models.DateTimeField(blank=True, default=timezone.now)
    fixed_date = models.DateTimeField(blank=True, null=True,)
    fix_version = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS, default=1)
    upvotes = models.ManyToManyField(User, blank=True, related_name="upvoted_tickets")
    # upvotes = models.IntegerField(default=0)
    devComments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ticketName
        
    def total_upvotes(self):
        return self.upvotes.count()    
