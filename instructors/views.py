from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from instructors.models import Instructor
from Courses.models import Course


def hello(request):
    courses = Course.objects.all()
    return render(request, "general.html", {"courses": courses})

def instructors_list(request):
    instructors = Instructor.objects.all()
    return render(request, "instructors_list.html", {"instructors": instructors})

def hello_python(request):
    return render(request, 'python.html' )

def http(request):
    response =  render(request, "http.html")
    return HttpResponseNotFound()

def sum_two(request, a, b):
    s = int(a) + int(b)
    return HttpResponse(s)

