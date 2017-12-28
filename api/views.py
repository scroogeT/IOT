# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .serializers import deviceSerializer
from .models import device

# Create your views here.

def index(request):
    return render(request, 'api/index.html')

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = device.objects.all()
    serializer_class = deviceSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = device.objects.all()
    serializer_class = deviceSerializer