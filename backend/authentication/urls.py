from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from authentication.api.viewsets import CustomUserViewSet, UserFavViewSet

router = DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('user-favs', UserFavViewSet)

urlpatterns = [
   path('',views.home, name= "home"),
   path('signup', views.signup, name="signup"),
   path("signin", views.signin, name="signin"),
   path("logout", auth_views.LogoutView.as_view(), name='logout'),
   path("fav/<int:user_id>/", views.fav, name="fav"),
   path("addfav", views.addfav, name="addfav"),
   path('api/', include(router.urls))
]