# rest_framework viewsets 지정 
from rest_framework import viewsets, filters 
from .models import * 
from .serializers import * 

class AlbumViewSet(viewsets.ModelViewSet): 
    queryset = Album.objects.all() 
    serializer_class = AlbumSerializer
    filter_backends = (filters.SearchFilter,) 
    search_fields = ('name')

class PhotoViewSet(viewsets.ModelViewSet): 
    queryset = Photo.objects.all() 
    serializer_class = PhotoSerializer

    