"""
URL configuration for attendance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student.views import *
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('' ,home ,name="home"),

    path('home/' ,home ,name="home"),

    path('index/' ,home ,name="home"),

    path('login/' ,login_page ,name="login_page"),

    path('register/' ,register ,name="register"),

#    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),

    path('logout/', logout_page, name='logout_page'),


    # Departmenr URLS

    path('ceone/', ceone, name='ceone'),

    path('student-list/', student_list, name='student_list'),

    path('cereport/', cereport, name='cereport'),

]
