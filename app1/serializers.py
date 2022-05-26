from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from .models import Album, Track




class AlbumSerializer(serializers.ModelSerializer):
     
    class Meta:
        model=Album
        fields='__all__'
        
        
class Trackserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Track
        fields='__all__'      