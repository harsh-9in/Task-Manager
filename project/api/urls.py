from django.urls import path,include

from rest_framework.routers import DefaultRouter

from api import views


router=DefaultRouter()
router.register('signup',views.UserProfileViewset)




urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.UserLogin.as_view()),
]