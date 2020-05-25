'''from rest_framework import routers
from .api import SolutionViewSet

router = routers.DefaultRouter()

router.register('api/solutions', SolutionViewSet, 'solutions')

urlpatterns = router.urls

'''

from django.urls import path
from solutions import views

urlpatterns = [
    path('solution/', views.solutionSubmissionView, name="solution-Submission-View"),
    path('vote/<str:pk>/', views.voteView, name='voting'),
]
