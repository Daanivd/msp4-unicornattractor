from django.shortcuts import render, get_object_or_404
from .models import Feature

# Create your views here.
def all_features(request):
    features = Feature.objects.all()
    return render(request, "features.html", {"features": features})
    
def feature_detail(request, pk):
    """
    Create a view that returns a single
    feature based on its id (pk) and
    render it to 'ticket.html' template.
    Or return a 404 error if
    not found
    """
    feature = get_object_or_404(Feature, pk=pk)
    feature.save()
    return render(request, "feature.html", {'feature': feature})      
