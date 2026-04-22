from django.shortcuts import render, redirect
from .models import Department, Course, Faculty, Section, Student
from .forms import DepartmentForm, CourseForm, FacultyForm, SectionForm, ClassListUploadForm
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
    sections = Section.objects.select_related('course').all()
    return render(request, 'core/sections.html', {'sections': sections})

def add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grading_system:section_list')  # or wherever you want
    else:
        form = SectionForm()

    faculty = Faculty.objects.all()

    return render(request, 'core/add_section.html', {
        'form': form,
        'faculty': faculty
    })

def class_list(request):
    sections = Section.objects.all()

    return render(request, 'core/class_list.html', {
        'sections': sections
    })

def section_detail(request, id):
    section = Section.objects.get(id=id)

    return render(request, 'core/section_detail.html', {
        'section': section
    })

def add_class_list(request):
    if request.method == "POST":
        form = ClassListUploadForm(request.POST)

        if form.is_valid():
            section = form.cleaned_data['section']
            data = form.cleaned_data['data']

            lines = data.strip().split("\n")

            for line in lines:
                parts = line.split("\t")  # Excel copy-paste uses TAB

                if len(parts) >= 2:
                    student_id = parts[0].strip()
                    name = parts[1].strip()

                    Student.objects.create(
                        student_id=student_id,
                        name=name,
                        section=section
                    )

            return redirect('grading_system:class_list')

    else:
        form = ClassListUploadForm()

    return render(request, 'core/add_class_list.html', {
        'form': form
    })