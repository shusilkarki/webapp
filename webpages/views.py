from django.shortcuts import render
from django.http import HttpResponse
from .models import Webpage

# Create your views here.


def index(request):
    webpages = Webpage.objects
    return render(request, 'index.html', {'webpages':webpages})

 