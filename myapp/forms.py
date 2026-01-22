from django import forms
from .models import Student


class Inputforms(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'rollno', 'password']


    
