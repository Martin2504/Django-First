from django.urls import path
from . import views

# A list of all the urls for this app.
urlpatterns = [
    path("", views.index, name="index")   # ('url', 'responding function', 'name of url pattern')
]