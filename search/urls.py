from django.urls import re_path
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView

from . import views

app_name = "search"

urlpatterns = [
    re_path(r'^$', views.index, name='main'),
    path("searchElsevier", views.search_elsevier, name='searchElsevier'),
    path("api/elsevier", views.api_search_elsevier, name='apiSearchElsevier'),
    path("searchArxiv", views.search_arxiv, name='searchArxiv'),
    path("api/arxiv", views.api_search_arxiv, name='apiSearchArxiv'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name="search:schema"), name='swagger-ui'),
]
