from rest_framework import viewsets
from authentication.models import CustomUser, UserFav
from .serializers import CustomUserSerializer, UserFavSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserFavViewSet(viewsets.ModelViewSet):
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer


