from django.contrib import admin 
from django.urls import path 
# from auction.views import AuctionView, SearchFormView, AuctionDetail

app_name="streaming"

urlpatterns = [ 
    path('',SearchFormView.as_view(),name="search")
    


]
