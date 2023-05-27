from rest_framework import serializers
from authentication.models import CustomUser, UserFav

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFav
        fields = '__all__'