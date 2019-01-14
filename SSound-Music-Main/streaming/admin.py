from django.contrib import admin
from streaming.models import * 
# Register your models here.

class MusicRegisterAdmin(admin.ModelAdmin): 
    list_display = ('artist','title','hashe')

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('email','profile_url')

admin.site.register(Music,MusicRegisterAdmin)
admin.site.register(Artist,ArtistAdmin)