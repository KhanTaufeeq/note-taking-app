from django.urls import path 
from . import views

urlpatterns = [
    path('', views.ListAllNotes.as_view()),
    path('add/',views.CreateNewNote.as_view()),
    path('<int:id>/', views.FetchOneNote.as_view()),
    path('<int:id>/', views.UpdateOneNote.as_view())
]

