from django.urls import path, include
from . import views
from api.views import *

urlpatterns = [
    #    path('register', views.UserRegister.as_view(), name='register'),

    path('bot/create', BotCreateView.as_view()),
    path('bot/all', BotsListView.as_view()),
    path('bot/detail/<int:pk>', BotDetailView.as_view()),
]
