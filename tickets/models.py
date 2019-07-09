from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Ticket(models.Model):
    """ A ticket """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='blog_posts')
    content = models.TextField()
    image = models.ImageField(upload_to="img", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.title
