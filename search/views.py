from django.shortcuts import render
from django.views.generic import TemplateView

from .elsevier_rest_class import Elsevier_rest

def index(request):
    return render(request, 'search/main.html')

def searchElsevier(request):
    rest = Elsevier_rest()
    
    q = request.POST.get('q')
    
    context = rest.basicQuery(q)
    
    return render(request, 'search/search_elsevier.html', context)
    