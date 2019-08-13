from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required

@login_required
def all_tickets(request, pk=None):
    """
    Create a view that will return a list
    of tickets that have been published up to now
    and render them to the 'tickets.html' template
    """
    tickets = Ticket.objects.all().order_by('-upvotes')
    
    """ In order to create new ticket through Modal, see 'create_or_edit_ticket function below' """
    form = TicketForm
    create_or_edit_ticket(request)
    
    return render(request, "tickets.html", {'tickets': tickets, 'form':form}) 


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
    """
    To edit ticket through modal, see 'create_or_edit_ticket function below
    """
    form = TicketForm(instance=ticket)
    create_or_edit_ticket(request, pk=pk)
    
    if request.method == 'GET':
        return render(request, "ticket.html", {'ticket': ticket, 'form':form}) 
    if request.method == 'POST':
        return redirect('ticket_detail', pk=pk)
    
 
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
            pk=ticket.pk
            
            messages.error(request, "Thank you, your ticket has been added/edited and passed on to our development team!")   

            return redirect('ticket_detail', pk=pk)
            
    else:
        form = TicketForm(instance=ticket)

    
@login_required
def ticket_upvote(request, pk):
    """User can upvote a ticket once, but not more than that. 
    If they do try they get a message explaining why they can't"""
    ticket = get_object_or_404(Ticket, pk=pk)
    if ticket.upvotes.filter(id=request.user.id).exists():
        ticket.upvotes.remove(request.user)
        is_upvoted = False
        messages.error(request, 'You already upvoted this!')
    else:
        ticket.upvotes.add(request.user)
        is_upvoted = True
    
    return redirect('ticket_detail', pk=pk)
            
            
        
    
