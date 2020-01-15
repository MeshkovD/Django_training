from django.urls import path, re_path
from django.shortcuts import render
from .views import quadratic_results


urlpatterns = [
    path('',  quadratic_results),

]