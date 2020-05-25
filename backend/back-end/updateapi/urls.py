from django.urls import path
from . import views

urlpatterns = [
    path('user-personal-view/', views.userPersonalView, name="user-personal-get-view"),
    path('user-personal-get-view/<str:pk>/', views.userPersonalGetView, name="user-personal-get-view"),
    path('user-professional-view/', views.userProfessionalView, name="user-professional-view"),
    path('user-professional-get-view/<str:pk>/', views.userProfessionalGetView, name="user-professional-get-view"),
	path('user-personal-create/', views.userPersonalCreateView, name="user-personal-create"),
    path('user-professional-create/', views.userProfessionalCreateView, name="user-professional-create"),
	path('user-personal-update/<str:pk>/', views.userPersonalUpdateView, name="user-personal-update"),
	path('user-professional-update/<str:pk>/', views.userProfessionalUpdateView, name="user-professional-update"),
]