from django.urls import re_path
from django.urls import path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='main'),
    path("searchElsevier", views.search_elsevier, name='searchElsevier'),
    path("api/elsevier", views.api_search_elsevier, name='apiSearchElsevier'),
    path("searchArxiv", views.search_arxiv, name='searchArxiv'),
    path("api/arxiv", views.api_search_arxiv, name='apiSearchArxiv'),
]
