from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import MovieSerializer
from .models import Movie

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
