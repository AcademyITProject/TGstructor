from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import datetime


class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('An email is required.')

        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class AppUser(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()

    is_staff = models.BooleanField(default=False)

    def is_staff(self):
        return self.is_staff

    def __str__(self):
        return self.username


class AppBot(models.Model):
    login_id = models.ForeignKey(AppUser, verbose_name='Login id', on_delete=models.CASCADE)
    app_name = models.CharField(verbose_name='App name', max_length=512)
    token = models.CharField(verbose_name='token', max_length=512)
    url = models.CharField(verbose_name='Url', max_length=512)
    name = models.CharField(verbose_name='Name', max_length=255)
    launch_status = models.BooleanField(verbose_name='Status', default=0)

    def __str__(self):
        return self.name


class TypesCommand(models.Model):
    type_name = models.CharField(verbose_name='name', max_length=512)


class Commands(models.Model):
    bot_id = models.ForeignKey(AppBot, verbose_name='bot_id', on_delete=models.CASCADE)
    command_name = models.CharField(verbose_name='name', max_length=512)
    type_id = models.ForeignKey(TypesCommand, verbose_name="type_id", on_delete=models.CASCADE)
    link_status = models.BooleanField(verbose_name='link_status', default=0)
    media_status = models.BooleanField(verbose_name='media_status', default=0)


class LinkCommands(models.Model):
    current_command = models.ForeignKey(Commands, verbose_name='curCmd', related_name='linkcommands_current',
                                        on_delete=models.CASCADE)
    following_command = models.ForeignKey(Commands, verbose_name='flwCmd', related_name='linkcommands_following',
                                          on_delete=models.CASCADE)


class Media(models.Model):
    command_id = models.ForeignKey(Commands, verbose_name='cmdId', on_delete=models.CASCADE)
    media = models.TextField(verbose_name="media")


class QuestionCommand(models.Model):
    command_id = models.ForeignKey(Commands, verbose_name='cmdId', on_delete=models.CASCADE)
    answer = models.TextField(verbose_name="answer")


class MailCommand(models.Model):
    command_id = models.ForeignKey(Commands, verbose_name='cmdId', on_delete=models.CASCADE)
    mail = models.TextField(verbose_name="mail")
    date = models.DateField(default=datetime.now)
