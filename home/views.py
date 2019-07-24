from django.shortcuts import render
from features.views import Feature
from tickets.views import Ticket

# Create your views here.
def index(request):
    """A view that displays the index page"""
    features = Feature.objects.filter(status=4)
    tickets = Ticket.objects.all()
    devFeatures = Feature.objects.filter(status=3)
    return render(request, "index.html", {"features": features, "devFeatures": devFeatures, 'tickets': tickets})
