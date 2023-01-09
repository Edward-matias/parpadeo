from rest_framework import serializers
from .models import post

class ParpadeoSerializer(serializers.ModelSerializer):
    class Meta:
        model=post
        fields=('id','fecha')
        #read_only_fields=('fecha')