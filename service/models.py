from django.db.models import Model, ForeignKey, CASCADE, BooleanField

from resume.models import Resume
from vacancy.models import Vacancy


class Application(Model):
    resume = ForeignKey(Resume, related_name='applications', on_delete=CASCADE)
    vacancy = ForeignKey(Vacancy, related_name='applications', on_delete=CASCADE)
    applied = BooleanField(default=False)

    def __str__(self):
        return (f'{self.vacancy.name} {self.resume.first_name} '
                f'{self.resume.last_name}---{self.resume.work_name}')
