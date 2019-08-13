from django.shortcuts import render
from tickets.models import Ticket
from tickets.forms import TicketForm

# Create your views here.
def ticket_search(request):
    tickets = Ticket.objects.filter(ticketName__icontains=request.GET['query'])
    form = TicketForm(instance=None)
    return render(request, "search_results.html", {"tickets": tickets, 'form':form})