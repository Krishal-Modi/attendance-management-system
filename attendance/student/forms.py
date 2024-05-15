from django import forms
from .models import *

class ContactForm(forms.Form):
    username = forms.CharField(max_length=20)
    date = forms.DateField()
    time = forms.TimeField()


# forms.py

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = ['date', 'status', 'time', 'username']