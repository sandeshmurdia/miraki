from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(
    r'profile',
    views.ProfileSpaceViewSet,
    basename='profile-space'
)

router.register(
    r'',
    views.SpaceViewSet,
    basename='space'
)


urlpatterns = [
    path('', include(router.urls)),
]