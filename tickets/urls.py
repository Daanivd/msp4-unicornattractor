from django.conf.urls import url
from .views import all_tickets, ticket_detail, create_or_edit_ticket, ticket_upvote

urlpatterns = [
    url(r'^$', all_tickets, name='all_tickets'),
    url(r'^(?P<pk>\d+)/$', ticket_detail, name='ticket_detail'),
    # url(r'^new/$', create_or_edit_ticket, name='new_ticket'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_ticket, name='new_ticket'),
    url(r'^(?P<pk>\d+)/upvote/$', ticket_upvote, name='ticket_upvote'),
    
]
