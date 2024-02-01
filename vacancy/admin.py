from django.contrib import admin
from django.contrib.admin import ModelAdmin

from vacancy.models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(ModelAdmin):
    list_display = ['user', 'company_name', 'name',
                    'city']
