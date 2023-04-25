from django.contrib import admin
from .models import AppUser, AppBot


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'last_login', 'is_superuser')


class BotAdmin(admin.ModelAdmin):
    list_display = ('login_id', 'app_name', 'token', 'url', 'name', 'launch_status')


admin.site.register(AppUser, UserAdmin)
admin.site.register(AppBot, BotAdmin)
