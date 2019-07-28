from django.shortcuts import render
from features.models import Feature
from tickets.models import Ticket
from cart.views import add_to_cart

# Create your views here.
def index(request):
    """A view that displays the index page"""
    features = Feature.objects.filter(status=4)
    productFeatures = Feature.objects.filter(status=2)
    devFeatures = Feature.objects.filter(status=3)
    tickets = Ticket.objects.all()
    
    return render(request, "index.html", {"features": features, 'productFeatures': productFeatures, "devFeatures": devFeatures, 'tickets': tickets})
