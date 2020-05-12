from rest_framework import serializers

from . import models


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Feed
        fields= ['id','user_profile', 'text', 'created_on']
        extra_kwargs={
            'user_profile':{'read_only': True}
        }