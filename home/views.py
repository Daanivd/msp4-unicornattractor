from django.shortcuts import render
from django.core import serializers
from features.models import Feature
from tickets.models import Ticket
from features.forms import featureForm
from cart.views import add_to_cart
from django.utils import timezone
from django.http import JsonResponse
import json



# Create your views here.
def index(request):
    """A view that displays the index page"""
    features = Feature.objects.filter(status=4)
    productFeatures = Feature.objects.filter(status=2)
    devFeatures = Feature.objects.filter(status=3)
    tickets = Ticket.objects.all()
  
    bugData = get_bugData()
    featureDevData, featureVarData = get_featureData()
    
    return render(request, "index.html", {"features": features, 'productFeatures': productFeatures, "devFeatures": devFeatures, 'tickets': tickets, 'featureDevData': featureDevData, 'featureVarData':featureVarData, 'bugData': bugData})


def get_bugData():
    bugs =  Ticket.objects.filter(status=3) 
    bugs_list = []
    for ticket in bugs:
        deltaT = ticket.fixed_date-ticket.published_date
        bugs_list.append(round(deltaT.total_seconds()/3600/24))
      
    bugs_list_set = list(set(bugs_list))
    count_list = ['Days to Resolve',]
    for n in bugs_list_set:
        count_list.append(bugs_list.count(n))
        
    bugT = ['bugT']  
    for bug in bugs_list_set:
        bugT.append(bug)
        
    bugData = [bugT, count_list]     
    
    return bugData
    
def get_featureData():  
    features = Feature.objects.filter(status=4).order_by('feature_added_date')
    flist = []
    dlist = ['Timeline',]
    nlist = ['Number of Features over Time',]
    
    for feature in features:
        flist.append(feature.version)
        dlist.append(str(feature.feature_added_date)[0:19])
    for i in range(0, len(dlist)-1):
        nlist.append(i+1)
       
    featureDevData = [dlist, nlist]   
    featureVarData = flist
    
    return featureDevData, featureVarData
    
    
    

# def fdata(request):
#     fdata = Feature.objects.all()
#     fdata = serializers.serialize('json', fdata)
#     d = json.loads(fdata)
#     return JsonResponse(d, safe=False)