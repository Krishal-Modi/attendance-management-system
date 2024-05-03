from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=20)
    date = forms.DateField()
    time = forms.TimeField()
