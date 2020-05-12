from django.urls import path,include

from rest_framework.routers import DefaultRouter

from api import views
from feed.views import FeedViewset


router=DefaultRouter()
router.register('signup',views.UserProfileViewset)
router.register('feed',FeedViewset)



urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.UserLogin.as_view()),
]