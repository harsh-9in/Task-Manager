from rest_framework import serializers

from . import models


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Feed
        fields= '__all__'
        extra_kwargs={
            'user_profile':{'read_only': True}
        }