from django import forms
from .models import Report
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'crime_type',
            'state',
            'lga',
            'location_description',
            'incident_description',
            'security_agency',
            'image'
        ]
        widgets = {
            'location_description': forms.Textarea(attrs={'rows': 2}),
            'incident_description': forms.Textarea(attrs={'rows': 4}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
