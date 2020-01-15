from django.db import models
from django.conf import settings
from Courses.models import Course

class Position(models.Model):
    name = models.CharField(max_length=50, help_text="This is name")
    def __str__(self):
        return '%s' % (self.name)
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'



class Instructor(models.Model):
    name = models.CharField( verbose_name='Instructor Name', max_length=50, help_text="This is name")
    surname = models.CharField(max_length=50)
    course = models.ManyToManyField(Course)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    phone = models.CharField(max_length=15, null=True, blank=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    gender = models.CharField(max_length=1, choices=[('m', 'Male'), ('f', 'Female'),])

    position = models.ForeignKey(Position, null=True, blank=True, on_delete='CASCADE')

    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete='CASCADE')

    def __str__(self):
        return '%s %s' % (self.name, self.surname)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

