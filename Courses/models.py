from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"



class Lesson(models.Model):
    """docstring for Lesson."""
    subject = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE, blank=True)
    order = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return '%s' % (self.subject)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


# from Courses.models import Course, Lesson
#
#         a = Course.objects.create(name='python course', short_description='Программирование на языке Python. Уровень 2. Продвинутый курс', description='Вы занимаетесь программированием и хотите повысить свою квалификацию или систематизировать имеющиеся знания и навыки? Хотите изучить перспективный язык программирования Python? Вы - системный администратор или IT-специалист и у Вас возникла необходимость в освоении данного языка программирования?')

# a = Lesson.objects.create(subject='Тема 1', description='Вводное занятие', course=python course)
# a = Lesson.objects.create(subject='Тема 2', description='MVC архитектура')

