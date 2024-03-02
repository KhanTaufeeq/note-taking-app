from django.urls import path 
from . import views

urlpatterns = [
    path('', views.ListAllNotes.as_view())
]

