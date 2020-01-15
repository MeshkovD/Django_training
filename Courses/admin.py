from django.contrib import admin
from Courses.models import Course, Lesson

class LessonInline(admin.StackedInline):
    model = Lesson
    fields = ["subject", "description"]

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
