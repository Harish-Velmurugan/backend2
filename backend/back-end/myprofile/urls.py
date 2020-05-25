from django.urls import path
from myprofile import views

urlpatterns = [
   path('<str:un>/', views.userProfileView, name="user-profile-view"),
   
]