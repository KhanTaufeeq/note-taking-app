from django.shortcuts import render
from . serializer import NoteSerializer
from . models import Note
from rest_framework import generics 
from rest_framework.mixins import ListModelMixin
# Create your views here.


class ListAllNotes(generics.ListAPIView):

    queryset = Note.objects.all() 
    serializer_class = NoteSerializer 

class CreateNewNote(generics.CreateAPIView):

    serializer_class = NoteSerializer 

class FetchOneNote(generics.RetrieveAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer 

    def get_object(self):
        id = self.kwargs['id'] 
        return self.get_queryset().get(pk = id) 
    

class UpdateOneNote(generics.UpdateAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
