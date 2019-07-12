from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required

@login_required
def get_tickets(request):
    """
    Create a view that will return a list
    of tickets that have been published up to now
    and render them to the 'tickets.html' template
    """
    tickets = Ticket.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "tickets.html", {'tickets': tickets})
 
@login_required    
def ticket_detail(request, pk):
    """
    Create a view that returns a single
    ticket based on its id (pk) and
    render it to 'ticket.html' template.
    Or return a 404 error if
    not found
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views += 1
    ticket.save()
    return render(request, "ticket.html", {'ticket': ticket})    

@login_required
def create_or_edit_ticket(request, pk=None):
    """
    Create a view that allows us to create
    or edit a ticket depending if the ticket-ID
    is null or not
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.author = request.user
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.save()
        
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticketform.html', {'form': form})