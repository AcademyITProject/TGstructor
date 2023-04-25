from django.contrib import admin
from .models import AppUser


# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'last_login', 'is_superuser')


admin.site.register(AppUser, PersonAdmin)
