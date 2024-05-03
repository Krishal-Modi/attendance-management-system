from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
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

"""
def delete_user(request, user_id):
    user_instance = get_object_or_404(User, id=user_id)
    
    # Save the username before deleting for the success message
    username = user_instance.username

    user_instance.delete()

    # Add a success message
    messages.success(request, f"User '{username}' deleted successfully!")

    return redirect('Login')
"""


# Department views


def ceone(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            CustomUser.objects.create(username=username, date=date, time=time)
            return redirect("/index/")  # Redirect to appropriate page
    else:
        form = ContactForm()
    return render(request, "ceone.html", {'form': form})