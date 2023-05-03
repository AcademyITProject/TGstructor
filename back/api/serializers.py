from rest_framework import serializers

from api.models import *


class BotDetailSerializer(serializers.ModelSerializer):
    #    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Bot
        fields = '__all__'  # Все поля сериализуем(работаем с ними)


class BotsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('app_name', 'token', 'url', 'name', 'launch_status', 'login_id')
