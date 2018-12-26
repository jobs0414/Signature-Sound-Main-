from django.conf.urls import url
from django.urls import path
from photo.views import * 

app_name = "photo"

urlpatterns = [
    
    path('', AlbumLV.as_view(), name='index'),
    path('album/', AlbumLV.as_view(), name='album_list'),
    path('album/<int:pk>', AlbumDV.as_view(),name='album_detail'),
    path('photo/<int:pk>', PhotoDV.as_view(), name='photo_detail'),


]