from dj_rest_auth.serializers import LoginSerializer
# from dj_rest_auth.registration.serializers import RegisterSerializer
# from rest_framework import serializers
from .models import User
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import authenticate, get_user_model


UserModel =get_user_model()
class NewUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = UserModel
        fields = ['pk', 'username', 'email', 'first_name', 'last_name']


# class NewRegisterSerializer(RegisterSerializer):
    # first_name = serializers.CharField()
    # last_name = serializers.CharField()
    # nickname = serializers.CharField()

    # def custom_signup(self, request, data):
    #     data.first_name = request.data['first_name']
    #     data.last_name = request.data['last_name']
    #     data.nickname = request.data['nickname']
    #     data.save()

    # def save(self, request):
    #     user = super().save(request)
    #     user.first_name = request.data['first_name']
    #     user.last_name = request.data['last_name']
    #     user.nickname = request.data['nickname']
    #     user.save()
    #     return user


class NewLoginSerializer(LoginSerializer):
    pass
