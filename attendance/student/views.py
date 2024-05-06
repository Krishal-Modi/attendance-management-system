from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import *
from .forms import *

# Create your views here.


def home(request):
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


# views.py

def ceone(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            
            # Save attendance for each student
            for student in students:
                status = request.POST.get(f"attendance_{student.id}")  # Get the attendance status
                # Ensure that the status is either 'absent' or 'present'
                if status in ['absent', 'present']:
                    StudentAttendance.objects.create(student=student, date=date, status=status)
                
            return redirect("/index/")  # Redirect to the appropriate page
    else:
        form = ContactForm()
    return render(request, "ceone.html", {'form': form, 'students': students})



"""
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_success')  # Redirect to a success page
    else:
        form = AttendanceForm()
    return render(request, 'attendance_form.html', {'form': form})
"""


def student_list(request):
    # Retrieve all students from the database
    students = Student.objects.all()
    
    # Pass the list of students to the template for rendering
    return render(request, 'ceone.html', {'students': students})