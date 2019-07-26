from django.conf.urls import url
from .views import ticket_search

urlpatterns = [
    url(r'^$', ticket_search, name='search')
]