from django.urls import path,include
from .views import TeamList,RacerList
from rest_framework.routers import DefaultRouter 
app_name="rank_api"
router = DefaultRouter()
router.register(r'teams', TeamList, basename='team')
router.register(r'racers',RacerList, basename='racer')

urlpatterns = [
    path('', include(router.urls)),
]