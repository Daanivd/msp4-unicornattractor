from django.test import TestCase
from django.contrib.auth.models import User
from tickets.models import Ticket



class TestSearch(TestCase):

    def test_search_(self):
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        ticket = Ticket(ticketName="Test Ticket", description='test-content', author=user)
        ticket.save()
        self.client.post
        page = self.client.get("/search/?query=unicorn",  follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "search_results.html")