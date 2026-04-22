from django.urls import path
from . import views

app_name = 'grading_system'

urlpatterns = [
    path('', views.grading_home, name='grading_home'),

    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.add_department, name='add_department'),

    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),

    path('faculty/', views.faculty_list, name='faculty_list'),
    path('faculty/add/', views.add_faculty, name='add_faculty'),

    path('sections/', views.section_list, name='section_list'),
    path('sections/add/', views.add_section, name='add_section'),

    path('class-list/', views.class_list, name='class_list'),
    path('add-class-list/', views.add_class_list, name='add_class_list'),

    path('section/<int:id>/', views.section_detail, name='section_detail'),
]