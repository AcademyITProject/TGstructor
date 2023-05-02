import genetics as genetics
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import permissions, status, generics
from .validations import custom_validation, validate_email, validate_password
from .models import AppBot
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    ##
    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    ##
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)


class BotCreateView(generics.CreateAPIView):
    serializer_class = BotDetailSerializer


class BotsListView(generics.ListAPIView):
    serializer_class = BotsListSerializer
    queryset = AppBot.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class BotDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BotDetailSerializer
    queryset = AppBot.objects.all()
    permissions_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class CommandCreateView(generics.CreateAPIView):
    serializer_class = CommandDetailSerializer


class CommandsListView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommandsListView
    queryset = Commands.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class CommandDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommandDetailSerializer
    queryset = Commands.objects.all()
    permissions_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class CommandLinkCreateView(generics.CreateAPIView):
    serializer_class = CommandLinkDetailSerializer


class CommandsLinkListView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommandsLinkListView
    queryset = LinkCommands.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class CommandLinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommandLinkDetailSerializer
    queryset = LinkCommands.objects.all()
    permissions_classes = (IsOwnerOrReadOnly, IsAuthenticated)
