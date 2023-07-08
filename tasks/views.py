from django.shortcuts import render

tasks = ["foo", "bar", "baz"]
# Create your views here.

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks  # The html template will have access to this variable when rendering.
    })

def add(request):
    return render(request, "tasks/add.html")