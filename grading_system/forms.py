from django import forms
from .models import Department, Course, Faculty

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['department', 'code', 'name', 'year_level', 'semester', 'credits']

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name']