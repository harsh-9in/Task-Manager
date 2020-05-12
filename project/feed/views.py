from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from feed import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from feed import serializers
from feed import models
from rest_framework.settings import api_settings 



class FeedViewset(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.FeedSerializer
    queryset=models.Feed.objects.all()
    permission_classes=[permissions.UpdateOwnStatus , IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save(user_profile=self.request.user)