from django.contrib import admin
from django.urls import path, re_path
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from instructors.views import hello, hello_python, sum_two, http, instructors_list
from Courses.views import course
from django.urls import include
from students.views import students_list, student


def results(request, a, b, c):
    list=[]
    list.append(a)
    list.append(b)
    list.append(c)
    print(list)

    for i in list:
        print(i)
    return HttpResponse(list)


urlpatterns = [
    path('', hello, name='home'),
    path('hello_python/', hello_python, name='hello_python' ),
    path('http/', http, name='http' ),
    re_path('sum/(?P<a>\d+)/(?P<b>\d+)/', sum_two, name='sum'),
    path('admin/', admin.site.urls),
    path('instructors_list/', instructors_list, name='instructors_list'),
    path('course/<int:id>/', course, name='course_url'),
    # path('results/(\d+)/', include('quadratic.urls')),
    re_path('results/a=(?P<a>\w+)&b=(?P<b>\w+)&c=(?P<c>\w+)/', results),
    path('students/', students_list, name='students_list'),
    path('student/<int:id>/', student, name='student'),
]
