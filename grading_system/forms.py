from django import forms
from .models import Department, Course, Faculty, Section

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

class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ['name', 'department', 'course', 'faculty']

class ClassListUploadForm(forms.Form):
    section = forms.ModelChoiceField(queryset=Section.objects.all())
    data = forms.CharField(widget=forms.Textarea, help_text="Paste Excel data here")