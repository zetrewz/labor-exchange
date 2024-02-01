from django.forms import ModelForm, TextInput

from resume.models import Resume


class ResumeCreateForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['first_name', 'last_name', 'work_name',
                  'about', 'photo', 'telephone',
                  'city', 'citizenship', 'salary',
                  'gender', 'experience']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'work_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Желаемая должность'}),
            'about': TextInput(attrs={'class': 'form-control', 'placeholder': 'О себе'}),
            'telephone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'Город'}),
            'citizenship': TextInput(attrs={'class': 'form-control', 'placeholder': 'Гражданство'}),
            'salary': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ожидания по зарплате'}),
            'experience': TextInput(attrs={'class': 'form-control', 'placeholder': 'Опыт работы'}),
        }
