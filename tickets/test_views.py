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
        ticket = Ticket(ticketName="Test Ticket", author=user)
        ticket.save()
        page = self.client.get("/tickets/{0}".format(ticket.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "ticket.html")  
        
    def test_edit_ticket(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        page = self.client.get("/tickets/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "ticketform.html")  
        
    def test_post_create_ticket(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        form = TicketForm(data={'author': user, 'content':'test content', 'ticketName': 'test title'})
        self.assertTrue(form.is_valid())
        page = self.client.post("/tickets/new/", {'author': user, 'content':'test content', 'ticketName': 'test title'}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "ticket.html")                                               
            
