from django.contrib.auth import get_user_model
from django.db.models import Manager, Model, ForeignKey, CASCADE, CharField, BooleanField, DateField, Index, \
    ManyToManyField, IntegerField, DateTimeField
from django.urls import reverse

User = get_user_model()


class PublishedManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Vacancy(Model):
    user = ForeignKey(User, on_delete=CASCADE,
                      related_name='vacancies')
    name = CharField(max_length=100)
    company_name = CharField(max_length=255)
    about = CharField(max_length=1000)
    responsibilities = CharField(max_length=1000)
    requirements = CharField(max_length=1000)
    conditions = CharField(max_length=1000)
    city = CharField(max_length=100)
    salary = IntegerField()
    created = DateTimeField(auto_now_add=True)
    publish = DateField(auto_now=True)
    active = BooleanField(default=True)
    in_favorites = ManyToManyField(User,
                                   related_name='favorites_vacancy',
                                   blank=True)
    objects = Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [Index(fields=['-publish']),
                   Index(fields=['name'])]

    def __str__(self):
        return f"{self.user.username} {self.name} {self.active}"

    def get_absolute_url(self):
        return reverse('vacancy:detail',
                       args=[self.id])
