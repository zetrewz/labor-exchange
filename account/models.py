from django.contrib.auth.models import AbstractUser
from django.db.models import Model, OneToOneField, CharField, CASCADE, BooleanField, ImageField


class User(AbstractUser):
    email_verify = BooleanField(default=False)


class EmployerProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE,
                         related_name='profile')
    first_name = CharField(max_length=100, blank=True)
    last_name = CharField(max_length=100, blank=True)
    about = CharField(max_length=1000, blank=True)
    photo = ImageField(upload_to='users/%Y/%m/%d/',
                       blank=True)

    def __str__(self):
        return f"{self.user.username} {self.first_name} {self.last_name}"
