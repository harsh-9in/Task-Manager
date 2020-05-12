from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from api import models
from api import serializers
from api import permissions
from rest_framework.authentication import TokenAuthentication



class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpadateOwnProfile,)


