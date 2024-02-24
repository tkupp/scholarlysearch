from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from .elsevier_rest_class import Elsevier_rest
from .arxiv_rest_class import Arxiv_rest

'''
The main page for the 'search' application.
'''
def index(request):
    return render(request, 'search/main.html')

'''
Pulls up the UI page for 'Elsevier' searching. 
'''
def search_elsevier(request):
    rest = Elsevier_rest()
    
    q = request.GET.get('q')
    num_pages = request.GET.get('num_pages')
    start_page = request.GET.get('start_page')
    
    context = rest.query(q, num_pages, start_page)
    
    return render(request, 'search/search_elsevier.html', context)
    

'''
The '@extend_schema decorator to generate the schema for swagger. 
This schema represents the Elseiver API search endpoint. 
'''
@extend_schema( 
        parameters=[
            OpenApiParameter( 
                name='q', 
                type={'type': 'string'}, 
                description="The search string",
                location=OpenApiParameter.QUERY, 
                required=True, 
            ),
            OpenApiParameter( 
                name='num_pages', 
                type={'type': 'integer'}, 
                description="The number of results to return.",
                location=OpenApiParameter.QUERY, 
                required=False, 
            ),
            OpenApiParameter( 
                name='start_page', 
                type={'type': 'integer'}, 
                description="Where you want the results to start from.",
                location=OpenApiParameter.QUERY, 
                required=False, 
            ),
        ], 
        responses={
            200: OpenApiTypes.OBJECT
        },
        examples=[
            OpenApiExample(
                name="Example Elsevier Search",
                summary="The results for an Elsevier search",
                description="Example Elsevier Search",
                value={
                    "status": 200,
                    "results": 16128,
                    "currentPage": 0,
                    "pageSize": 1,
                    "resultRows": [
                        {
                            "identifier": "DOI:10.1016/j.infoandorg.2024.100503",
                            "url": "https://api.elsevier.com/content/article/pii/S1471772724000034",
                            "title": "Generative mechanisms of AI implementation: A critical realist perspective on predictive maintenance",
                            "creator": "Alexander Stohr",
                            "publication": "Information and Organization",
                            "loadDate": "24-02-21" 
                        },
                    ]
                    
                },
            response_only=True
            )
        ],
    ) 
@api_view(['GET'])
def api_search_elsevier(request): 
    if request.method == 'GET':
        rest = Elsevier_rest()
    
        q = request.GET.get('q')
        num_pages = request.GET.get('num_pages')
        start_page = request.GET.get('start_page')
    
        context = rest.query(q, num_pages, start_page) 
        
        return Response(context)
    
    
'''
Pulls up the UI page for 'Arxiv' searching. 
'''    
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