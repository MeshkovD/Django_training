from django.shortcuts import render
from students.models import Student
# from django.http import HttpResponse

def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {"students": students})
