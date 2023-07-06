from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request) :    # request argument represents the HTPP request 
    return HttpResponse("Hello, world!")


