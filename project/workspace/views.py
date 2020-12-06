from django.shortcuts import render
from .models import Board
from . import serializers
from rest_framework import viewsets

# Create your views here.

class BoardViewsets(viewsets.ModelViewSet):
    serializer_class=serializers.BoardSerializer
    queryset=Board.objects.all()
