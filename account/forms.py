from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, PasswordInput, CharField, Select, EmailField, TextInput, ImageField, \
    ClearableFileInput
from django.utils.html import format_html

from account.models import EmployerProfile

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    email = EmailField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'e-mail'}))
    password1 = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
    user_type = CharField(widget=Select(
        choices=[('W', 'Работник'), ('E', 'Работодатель')]))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'user_type']


class UserLoginForm(ModelForm):
    email = EmailField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'e-mail'}))
    password = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ['email', 'password']


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = "Удалить"
    initial_text = "Сейчас"
    input_text = "Изменить"

    def format_value(self, value):
        if value and hasattr(value, "url"):
            return format_html('<a href="{}" target="_blank">{}</a>', value.url, 'Фото')
        return super().format_value(value)


class ProfileEditForm(ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['first_name', 'last_name', 'about', 'photo']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'about': TextInput(attrs={'class': 'form-control'}),
            'photo': CustomClearableFileInput(attrs={'class': 'form-control'})
        }
