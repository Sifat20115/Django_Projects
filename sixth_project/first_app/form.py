from django import forms
from first_app.models import *

class stu(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll','address','father_name']