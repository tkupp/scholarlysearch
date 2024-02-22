from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status

from .elsevier_rest_class import Elsevier_rest
from .arxiv_rest_class import Arxiv_rest
from .api_swagger import Elseiver_api_response

q_param = openapi.Parameter('q', openapi.IN_QUERY, description="Enter search query", type=openapi.TYPE_STRING, required=True)
num_pages_param = openapi.Parameter('num_pages', openapi.IN_QUERY, description="The number of pages to return", type=openapi.TYPE_INTEGER, required=False)
start_page_param = openapi.Parameter('start_page', openapi.IN_QUERY, description="The page to start returning results from", type=openapi.TYPE_INTEGER, required=False)

def index(request):
    return render(request, 'search/main.html')

def search_elsevier(request):
    rest = Elsevier_rest()
    
    q = request.GET.get('q')
    num_pages = request.GET.get('num_pages')
    start_page = request.GET.get('start_page')
    
    context = rest.query(q, num_pages, start_page)
    
    return render(request, 'search/search_elsevier.html', context)
    

@swagger_auto_schema(method='get', manual_parameters=[q_param, num_pages_param, start_page_param], responses={200: Elseiver_api_response})
@api_view(['GET'])
def api_search_elsevier(request):
    if request.method == 'GET':
        rest = Elsevier_rest()
    
        q = request.GET.get('q')
        num_pages = request.GET.get('num_pages')
        start_page = request.GET.get('start_page')
    
        context = rest.query(q, num_pages, start_page) 
        
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