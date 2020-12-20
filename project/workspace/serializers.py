from rest_framework import serializers
from . import models


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Board
        fields=['id','title', 'description', 'created_by']

        extra_kwargs = {
            'created_by': {'read_only': True}
        }


        
