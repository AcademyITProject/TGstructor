from django.urls import path, include
from . import views
from user_api.views import *

urlpatterns = [
    path('register', views.UserRegister.as_view(), name='register'),
    path('login', views.UserLogin.as_view(), name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
    path('user', views.UserView.as_view(), name='user'),

    path('base-auth/', include('rest_framework.urls')),

    path('bot/create', BotCreateView.as_view()),
    path('bot/all', BotsListView.as_view()),
    path('bot/detail/<int:pk>', BotDetailView.as_view()),
]
