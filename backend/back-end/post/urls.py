from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('',views.PostView)
urlpatterns = [
    path('',include(router.urls)),
    #path('bookmarks/<str:un>/<str:pid>/',views.bookmarks)
]