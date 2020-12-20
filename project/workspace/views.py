from django.shortcuts import render
from .models import Board
from . import serializers
from feed.models import UserProfile
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

# Create your views here.

class BoardViewsets(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class=serializers.BoardSerializer
    queryset = Board.objects.all()
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(created_by=self.request.user)

