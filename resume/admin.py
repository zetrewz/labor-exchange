from django.contrib import admin
from django.contrib.admin import ModelAdmin

from resume.models import Resume


@admin.register(Resume)
class ResumeAdmin(ModelAdmin):
    list_display = ['user', 'work_name', 'city',
                    'first_name', 'last_name']
