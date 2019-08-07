from django.test import TestCase
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_get_tickets_page(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        page = self.client.get("/tickets/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "tickets.html")
        
    def test_ticket_detail(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        ticket = Ticket(ticketName="Test Ticket", description='test-content', author=user)
        ticket.save()
        page = self.client.get("/tickets/{0}".format(ticket.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "ticket.html")  
        
    def test_edit_ticket(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        page = self.client.post('/tickets/edit/', {'author': user, 'description':'test content2', 'ticketName': 'test title2'}, follow=True)
      
    def test_create_ticket(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        page = self.client.post('/tickets/new/', {'author': user, 'description':'test content', 'ticketName': 'test title'}, follow=True)
    
     
    def test_upvote(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        ticket = Ticket(ticketName="Test Ticket", description='test-content', author=user)
        ticket.save()
        self.assertEqual(ticket.upvotes, 0)
        page = self.client.get("/tickets/{0}/upvote/".format(ticket.id), follow=True)
        self.assertEqual(ticket.upvotes, 1)
     
        
            
