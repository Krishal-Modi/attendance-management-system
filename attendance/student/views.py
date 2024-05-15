from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import *
from .forms import *
from django.urls import reverse
# Create your views here.


def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('/register/')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        messages.info(request, 'Account created successfully')
        return redirect('/login/')

    return render(request, 'register.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')  # Redirect to home page upon successful login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('/login/')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')


# Department views


# Computer Engineering Department

def ceone(request):
    students = Student.objects.all()
    distinct_dates = StudentAttendance.objects.order_by().values('date').distinct()

    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')
        time = request.POST.get('time')

        for student in students:
            status = request.POST.get(f"attendance_{student.id}")
            if status in ['absent', 'present']:
                StudentAttendance.objects.update_or_create(
                    student=student, date=date,
                    defaults={'status': status, 'time': time, 'username': username}
                )
        return redirect(reverse("cereport"))
    else:
        form = AttendanceForm()
    
    student_attendance = {student.id: {att.date: att for att in StudentAttendance.objects.filter(student=student)} for student in students}
    
    return render(request, "ceone.html", {
        'form': form,
        'students': students,
        'distinct_dates': [d['date'] for d in distinct_dates],
        'student_attendance': student_attendance,
    })




def student_list(request):
    # Retrieve all students from the database
    students = Student.objects.all()
    
    # Pass the list of students to the template for rendering
    return render(request, 'ceone.html', {'students': students})


# Appearing the Result of the student
def get_student_attendance(student, distinct_dates):
    attendance_records = {}
    for date in distinct_dates:
        attendance = student.studentattendance_set.filter(date=date).first()
        attendance_records[date] = attendance.status if attendance else ''
    return attendance_records


def cereport(request):
    students = Student.objects.all()
    distinct_dates = StudentAttendance.objects.values_list('date', flat=True).distinct()
    
    student_attendance = {}
    for student in students:
        attendance_records = StudentAttendance.objects.filter(student=student)
        attendance_data = {}
        for record in attendance_records:
            attendance_data[record.date] = {
                'status': record.status,
                'time': record.time,
                'username': record.username
            }
        student_attendance[student.id] = attendance_data
    
    return render(request, 'cereport.html', {'students': students, 'distinct_dates': distinct_dates, 'student_attendance': student_attendance})