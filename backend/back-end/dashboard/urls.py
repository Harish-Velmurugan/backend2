from django.urls import path
from dashboard import views

urlpatterns = [
   #path('dashboard-piv-view/', views.problemInvolvedView, name="dashboard-piv-view"),
   path('dashboard-ppp-view/<str:pk>/', views.dashboardPPView, name="dashboard-piv-view"),
   path('dashboard-ppo-view/<str:pk>/', views.postedProblemView, name="dashboard-ppo-view"),
   #path('user-professional-create/', views.userProfessionalCreateView, name="user-professional-create"),
   #path('user-personal-update/<                                                                                                                                                                                                                                                                                                 str:pk>/', views.userPersonalUpdateView, name="user-personal-update"),
   #path('user-professional-update/<str:pk>/', views.userProfessionalUpdateView, name="user-professional-update"),
]