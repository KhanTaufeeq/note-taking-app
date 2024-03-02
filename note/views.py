from django.shortcuts import render
from . serializer import NoteSerializer
from . models import Note
from rest_framework import generics
# Create your views here.


class ListAllNotes(generics.ListCreateAPIView):

    queryset = Note.objects.all() 
    serializer_class = NoteSerializer 
