from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .elsevier_rest_class import Elsevier_rest
from .arxiv_rest_class import Arxiv_rest

def index(request):
    return render(request, 'search/main.html')

def search_elsevier(request):
    rest = Elsevier_rest()
    
    q = request.GET.get('q')
    
    context = rest.basic_query(q)
    
    return render(request, 'search/search_elsevier.html', context)
    
@api_view(['GET'])
def api_search_elsevier(request):
    if request.method == 'GET':
        rest = Elsevier_rest()
    
        q = request.GET.get('q')
    
        context = rest.basic_query(q) 
        
        return Response(context)
    
def search_arxiv(request):
    rest = Arxiv_rest()
    
    q = request.GET.get('q')
    
    context = rest.basicQuery(q)
    
    return render(request, 'search/search_arxiv.html', context)
    
@api_view(['GET'])
def api_search_arxiv(request):
    if request.method == 'GET':
        rest = Arxiv_rest()
    
        q = request.GET.get('q')
    
        context = rest.basicQuery(q) 
        
        return Response(context)    