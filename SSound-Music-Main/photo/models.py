from django.db import models

# Create your models here.
# from __future__ import unicode_literals 
from django.utils.encoding import python_2_unicode_compatible
from django.db import models 
from django.urls import reverse 
from photo.fields import ThumbnailImageField #사진에 대한 원본 이미지와 썸네일 이미지 모두 저장 



@python_2_unicode_compatible
class Album(models.Model): 
    name = models.CharField(max_length=50)
    description = models.CharField('Several Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name 

    def get_absolute_url(self): 
        return reverse('photo:album_detail',args=(self.id))
        
@python_2_unicode_compatible

class Photo(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('photo Description',blank=True)
    upload_date = models.DateTimeField('Upload Date',auto_now_add=True)

    class Meta: 
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('photo:photo:detail',args=(self.id,))






