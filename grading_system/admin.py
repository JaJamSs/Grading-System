from django.contrib import admin
from .models import Department, Course, Faculty, Section, Student

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Section)
admin.site.register(Student)
