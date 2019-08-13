from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Feature
from .forms import featureForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def all_features(request):
    features = Feature.objects.filter(status=4)
    productFeatures = Feature.objects.filter(status=2)
    devFeatures = Feature.objects.filter(status=3)
    form = featureForm
    request_feature(request, pk=None)
    
    return render(request, 'features.html', {'features': features, 'productFeatures': productFeatures, 'devFeatures': devFeatures, 'form': form})
     
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
    return render(request, 'feature.html', {'feature': feature})  
    
@login_required
def request_feature(request, pk):
    """
    Request a feature by user
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == 'POST':
        form = featureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
                    feature = form.save(commit=False)
                    feature.author = request.user
                    feature.save()
        messages.error(request, "Thank you, your suggested feature has been passed on to our developer team!")            
       

    

