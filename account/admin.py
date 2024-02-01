from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from account.models import EmployerProfile

User = get_user_model()

admin.site.register(User, UserAdmin)


@admin.register(EmployerProfile)
class EmployerProfileAdmin(ModelAdmin):
    list_display = ['user']
    raw_id_fields = ['user']
