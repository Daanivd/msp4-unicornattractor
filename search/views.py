from django.shortcuts import render
from tickets.models import Ticket

# Create your views here.
def ticket_search(request):
    tickets = Ticket.objects.filter(ticketName__icontains=request.GET['query'])
    return render(request, "tickets.html", {"tickets": tickets})