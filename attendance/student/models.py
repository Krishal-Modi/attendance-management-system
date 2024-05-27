from django.db import models
from django.contrib.auth.models import *
from .models import *

# Create your models here.

class Admin(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='admin_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='admin_permissions')
    username = models.CharField(max_length=20, null=True, unique=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
    username = models.CharField(max_length=20, null=True, unique=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)



# Computer Engineering
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    status = models.CharField(max_length=100, default='pending')

    def __str__(self):
        return self.name

class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=100, default='pending')
    time = models.TimeField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
    
    
    
# Information Technology
class Studentit(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    status = models.CharField(max_length=100, default='pending')

    def __str__(self):
        return self.name

class StudentAttendanceit(models.Model):
    student = models.ForeignKey(Studentit, on_delete=models.CASCADE)  # Ensure this references Studentit
    date = models.DateField()
    status = models.CharField(max_length=100, default='pending')
    time = models.TimeField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
    

   
# Mechanical Engineering
class Studentme(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    status = models.CharField(max_length=100, default='pending')

    def __str__(self):
        return self.name

class StudentAttendanceme(models.Model):
    student = models.ForeignKey(Studentme, on_delete=models.CASCADE)  # Ensure this references Studentit
    date = models.DateField()
    status = models.CharField(max_length=100, default='pending')
    time = models.TimeField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"



# Civil Engineering

class Studentcv(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    status = models.CharField(max_length=100, default='pending')

    def __str__(self):
        return self.name

class StudentAttendancecv(models.Model):
    student = models.ForeignKey(Studentcv, on_delete=models.CASCADE)  # Ensure this references Studentit
    date = models.DateField()
    status = models.CharField(max_length=100, default='pending')
    time = models.TimeField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"



# Aeronautical Engineering

class Studentae(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    status = models.CharField(max_length=100, default='pending')

    def __str__(self):
        return self.name

class StudentAttendanceae(models.Model):
    student = models.ForeignKey(Studentae, on_delete=models.CASCADE)  # Ensure this references Studentit
    date = models.DateField()
    status = models.CharField(max_length=100, default='pending')
    time = models.TimeField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"



# Electrical Engineering

class Studentee(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    status = models.CharField(max_length=100, default='pending')

    def __str__(self):
        return self.name

class StudentAttendanceee(models.Model):
    student = models.ForeignKey(Studentee, on_delete=models.CASCADE)  # Ensure this references Studentit
    date = models.DateField()
    status = models.CharField(max_length=100, default='pending')
    time = models.TimeField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
