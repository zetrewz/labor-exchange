from django.contrib.auth import get_user_model
from django.db.models import Model, TextChoices, OneToOneField, DateTimeField, CharField, CASCADE, \
    ManyToManyField, TextField, ImageField, IntegerField
from django.urls import reverse

User = get_user_model()


class Resume(Model):
    class GenderChoices(TextChoices):
        Man = 'M', 'Man'
        Woman = 'W', 'Woman'

    user = OneToOneField(User, on_delete=CASCADE, related_name='resume')
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    work_name = CharField(max_length=100)
    about = TextField()
    photo = ImageField(upload_to='users/%Y/%m/%d/',
                       blank=True)
    telephone = IntegerField()
    city = CharField(max_length=100)
    citizenship = CharField(max_length=100)
    salary = IntegerField(blank=True)
    gender = CharField(max_length=20, choices=GenderChoices.choices)
    experience = TextField(blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    in_favorites = ManyToManyField(User,
                                   related_name='favorites_resume',
                                   blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.work_name}'

    def get_absolute_url(self):
        return reverse('resume:detail',
                       args=[self.pk])
