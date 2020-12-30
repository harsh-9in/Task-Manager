from rest_framework import serializers

from feed.models import Feed,Cards


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feed
        fields= '__all__'
        extra_kwargs={
            'user_profile':{'read_only': True}
        }



class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cards
        fields='__all__'



