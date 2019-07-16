from django.test import TestCase
from .models import Ticket
from django.contrib.auth.models import User


class TestTicketModel(TestCase):

    def test_status_defaults_to_open(self):
        user = User.objects.create_user(username='test_user', password='password')
        ticket = Ticket(ticketName="Test Ticket", author=user)
        ticket.save()
        self.assertEqual(ticket.ticketName, "Test Ticket")
        self.assertEqual(ticket.status, 1)
    
    def test_ticket_as_a_string(self):
            ticket = Ticket(ticketName="Test Ticket")
            self.assertEqual("Test Ticket", str(ticket))
