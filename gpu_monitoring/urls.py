from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from gpu_monitoring.views import VideoViewSet,RatingViewSet,UserViewSet

router = routers.DefaultRouter()
# api/video/
router.register('videos',VideoViewSet)
router.register('ratings',RatingViewSet)
router.register('users',UserViewSet)
urlpatterns = [
 path('',include(router.urls))
]