from rest_framework import routers 
from photo.viewsets import * 

router = routers.DefaultRouter() 

router.register('album',AlbumViewSet)
router.register('photo',PhotoViewSet)

