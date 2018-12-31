from rest_framework import serializers
from .models import * 

# models 단순화 

class AlbumSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Album
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Photo 
        fields = '__all__'


        
