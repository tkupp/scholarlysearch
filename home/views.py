from django.shortcuts import render
from django.views.generic import TemplateView
import os

def index(request):

    return render(request, 'index.html')

