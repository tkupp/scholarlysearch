from django.urls import re_path
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
        ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^$', views.index, name='main'),
    path("searchElsevier", views.search_elsevier, name='searchElsevier'),
    path("api/elsevier", views.api_search_elsevier, name='apiSearchElsevier'),
    path("searchArxiv", views.search_arxiv, name='searchArxiv'),
    path("api/arxiv", views.api_search_arxiv, name='apiSearchArxiv'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
