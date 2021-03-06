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
        
    def test_create_ticket_form(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        ticketform = TicketForm(data={'ticketName': "testTicket", 'description': "testDescription"})
        self.assertTrue(ticketform.is_valid())
        
    def test_create_ticket_missing_field(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        ticketform = TicketForm(data={'ticketName': "", 'description': "testDescription"})
        self.assertFalse(ticketform.is_valid())
        
    def test_create_ticket(self):
        user = User.objects.create_user(username='test_user', password='password')
        login = self.client.login(username='test_user', password='password')
        self.assertTrue(login)
        page = self.client.post('/tickets/new/', {'author': user, 'description':'test content', 'ticketName': 'test title'})
        
    def test_edit_ticket(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        page = self.client.post('/tickets/edit/', {'author': user, 'description':'test content2', 'ticketName': 'test title2'})
      
    # def test_upvote_ticket(self):
    #     user = User.objects.create_user(username='username', password='password')
    #     login = self.client.login(username='username', password='password')
    #     self.assertTrue(login)
    #     ticket = Ticket(ticketName='Test Ticket', description='test-content', author=user)
    #     ticket.save()
    #     self.assertEqual(ticket.upvotes, 0)
    #     self.assertEqual(ticket.total_upvotes, 0)
        
    #     page = self.client.post("/tickets/{0}/upvote".format(ticket.id), follow=True)
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "tickets.html")
    #     self.assertEqual(ticket.total_upvotes, 1)
        
            
