from django.db import models
from Courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    email = models.EmailField(help_text='A valid email address, please.')
    phone = models.CharField(max_length=25)
    addres = models.CharField(max_length=50)
    skype = models.CharField(max_length=25)
    courses = models.ManyToManyField(Course)



    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
