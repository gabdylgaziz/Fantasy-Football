from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import *

router = DefaultRouter()
router.register("club", ClubViewSet)
router.register("footballer", FootballerViewSet)

 
urlpatterns = [ 
    path('top', getTopPlayers),
    path('club/<int:id>/', getClub),
    path('footballer/<int:id>/', getFootballer),
    path('', include(router.urls)),
]