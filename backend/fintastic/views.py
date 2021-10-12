from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FintasticSerializer
from .models import Fintastic

# Create your views here.

class FintasticView(viewsets.ModelViewSet):
    serializer_class = FintasticSerializer
    queryset = Fintastic.objects.all()
