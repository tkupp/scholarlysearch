from django.urls import re_path
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Scholarly Search API')

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='main'),
    path("searchElsevier", views.searchElsevier, name='searchElsevier'),
    path("swagger", schema_view)
]
