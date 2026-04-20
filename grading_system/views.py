from django.shortcuts import render, redirect
from .models import Department, Course, Faculty
from .forms import DepartmentForm, CourseForm, FacultyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render


# Redirect root URL to dashboard
@login_required(login_url='login')
def home(request):
    return redirect('dashboard_test')  # Automatically go to dashboard

@login_required(login_url='login')
def dashboard_test_view(request):
    return render(request, 'core/dashboard_test.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_test')  # Send user directly to dashboard

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard_test')  # After login → dashboard
        else:
            return render(request, 'core/login.html', {'form': form})

    form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    # Always redirect after logout, regardless of GET or POST
    return redirect('login')

def grading_home(request):
    return render(request, 'core/grading_home.html')

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'core/departments.html', {
        'departments': departments
    })

## DEPARTMENT ##

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'core/departments.html', {
        'departments': departments
    })

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grading_system:department_list')
    else:
        form = DepartmentForm()

    return render(request, 'core/add_department.html', {
        'form': form
    })

## COURSE/SUBJECT ##

def course_list(request):
    courses = Course.objects.select_related('department').all()
    return render(request, 'core/courses.html', {'courses': courses})

def course_list(request):
    departments = Department.objects.prefetch_related('courses').all()
    return render(request, 'core/courses.html', {
        'departments': departments
    })

def add_course(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('grading_system:course_list')

    return render(request, 'core/add_course.html', {'form': form})

## FACULTY ##

def faculty_list(request):
    faculty = Faculty.objects.all()
    return render(request, 'core/faculty.html', {'faculty': faculty})


def add_faculty(request):
    form = FacultyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('grading_system:faculty_list')

    return render(request, 'core/add_faculty.html', {'form': form})


def section_list(request):
    sections = Section.objects.select_related('course', 'faculty').all()
    return render(request, 'core/sections.html', {'sections': sections})


def add_section(request):
    form = SectionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('grading_system:section_list')

    return render(request, 'core/add_section.html', {'form': form})