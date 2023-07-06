from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# request argument represents the HTPP request 
def index(request) :            #.../hello/
    return HttpResponse("Hello, world!")

def martin(request):            #.../hello/martin
    return HttpResponse("Hello Martin!")

def david(request):             #.../hello/david
    return HttpResponse("Hello David!")

def greet(request, name):       #.../hello/{name}
    return HttpResponse(f"Hello, {name.capitalize()}!")

def renderer(request):            #.../hello/renderer
    return render(request, "hello/index.html")  # Returning an HTML Template. 

def renderGreet(request, name):     #.../hello/render/{name}
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    } )    # Optional template 3rd argument 'context'. 
           # All the variables I want the template to have access to. 
