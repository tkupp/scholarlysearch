from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view

from .elsevier_rest_class import Elsevier_rest

schema_view = get_swagger_view(title='Scholarly Search API')

def index(request):
    return render(request, 'search/main.html')

def searchElsevier(request):
    rest = Elsevier_rest()
    
    q = request.GET.get('q')
    
    context = rest.basicQuery(q)
    
    return render(request, 'search/search_elsevier.html', context)
    