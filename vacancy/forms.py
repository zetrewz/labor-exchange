from django.forms import ModelForm, TextInput

from vacancy.models import Vacancy


class VacancyCreateForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'company_name', 'about', 'responsibilities',
                  'requirements', 'conditions', 'city',
                  'salary', 'active']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Должность'}),
            'company_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Компания'}),
            'about': TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'responsibilities': TextInput(attrs={'class': 'form-control', 'placeholder': 'Обязанности'}),
            'requirements': TextInput(attrs={'class': 'form-control', 'placeholder': 'Требования'}),
            'conditions': TextInput(attrs={'class': 'form-control', 'placeholder': 'Условия'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'Город'}),
            'salary': TextInput(attrs={'class': 'form-control', 'placeholder': 'Зарплата в RUB'}),
        }
