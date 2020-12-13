from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from feed.permissions import UpdateOwnStatus
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from feed import serializers
from feed.models import Feed
from rest_framework.settings import api_settings



class FeedViewset(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.FeedSerializer
    def get_queryset(self):
        return Feed.objects.filter(user_profile=self.request.user)
    permission_classes=[UpdateOwnStatus, IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save(user_profile=self.request.user)
