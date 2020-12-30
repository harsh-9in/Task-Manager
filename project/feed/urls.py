from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views



router=DefaultRouter()
router.register('feed',views.FeedViewset,basename='feed')
router.register('card',views.CardViewset,basename='card')



urlpatterns = [
    path('',include(router.urls)),
]
