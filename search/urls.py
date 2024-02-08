from django.urls import re_path
from django.urls import path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='main'),
    path("searchElsevier", views.searchElsevier, name='searchElsevier'),
    path("api/elsevier", views.apiSearchElsevier, name='apiSearchElsevier'),
]
