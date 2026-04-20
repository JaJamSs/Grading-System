from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
## COURSE/ SUBJECT ##

class Course(models.Model):
    YEAR_LEVELS = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
    ]

    SEMESTERS = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
    ]

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    year_level = models.CharField(max_length=1, choices=YEAR_LEVELS)
    semester = models.CharField(max_length=1, choices=SEMESTERS)
    credits = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"
    
## FACULTY ##

class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name