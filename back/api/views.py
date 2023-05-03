from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics

from api.serializers import *


# Create your views here.


class BotCreateView(generics.CreateAPIView):
    serializer_class = BotDetailSerializer


class BotsListView(generics.ListAPIView):
    serializer_class = BotsListSerializer
    queryset = Bot.objects.all()


class BotDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BotDetailSerializer
    queryset = Bot.objects.all()


class BotDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BotDetailSerializer
    queryset = Bot.objects.all()
