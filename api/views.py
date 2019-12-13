from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Wordserializer
from words.models import Words

class WordsView(viewsets.ModelViewSet):
    querset =  Words.objects.all()
    serializer = Wordserializer
