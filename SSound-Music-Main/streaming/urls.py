from django.contrib import admin 
from django.urls import path 
from streaming.views import *

app_name="streaming"

urlpatterns = [ 
    path('',MusicStreaming.as_view(),name='index'),
    path('search',SearchFormView.as_view(),name="search"),
    path('main',MusicMain.as_view(),name="main"),

]
