from django.contrib import admin 
from django.urls import path 
from streaming.views import SearchFormView,StreamingView

app_name="streaming"

urlpatterns = [ 
    path('', StreamingView.as_view(), name="streaming"),
    path('search/',SearchFormView.as_view(),name="streaming:search"),
    


]
