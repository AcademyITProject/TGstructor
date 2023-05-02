from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from user_api.models import *

UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'])
        user_obj.username = clean_data['username']
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    ##
    def check_user(self, clean_data):
        user = authenticate(username=clean_data['email'], password=clean_data['password'])
        if not user:
            raise ValidationError('user not found')
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username')


class BotDetailSerializer(serializers.ModelSerializer):
    #    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AppBot
        fields = '__all__'  # Все поля сериализуем(работаем с ними)


class BotsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppBot
        fields = ('app_name', 'token', 'url', 'name', 'launch_status', 'login_id')


class CommandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commands
        fields = '__all__'


class CommandsListView(serializers.ModelSerializer):
    class Meta:
        model = AppBot
        fields = ('bot_id', 'command_name', 'type_id', 'link_status', 'media_status')


class CommandLinkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkCommands
        fields = '__all__'


class CommandsLinkListView(serializers.ModelSerializer):
    class Meta:
        model = LinkCommands
        fields = ('current_command', 'following_command')
