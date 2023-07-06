from django.urls import path
from . import views

# A list of all the urls for this app.
urlpatterns = [
    path("", views.index, name="index"),   # ('url', 'responding function', 'name of url pattern')
    path("martin", views.martin, name="martin"),
    path("david", views.david, name="david"),
    path("renderer", views.renderer, name="renderer"),
    path("<str:name>", views.greet, name="greet"),
    path("render/<str:name>", views.renderGreet, name="renderGreet")
    
]