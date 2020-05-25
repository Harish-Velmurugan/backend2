from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [

   path('',views.SearchAPIView.as_view({'get':'list'}))


]