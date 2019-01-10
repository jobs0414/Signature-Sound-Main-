from django.contrib import admin 
from django.urls import path 
from streaming.views import SearchFormView

app_name="streaming"

urlpatterns = [ 
    path('',SearchFormView.as_view(),name="search")
    


]
