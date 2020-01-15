from django.shortcuts import render
from Courses.models import Course

def course(request, id):
    # course = Course.objects.filter(id = 'id')
    course = Course.objects.get(id__iexact=id)
    return render(request, 'course.html', context={'course':course})
