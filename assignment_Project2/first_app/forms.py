from django import forms
from first_app.models import taskFormModel

class taskForm(forms.ModelForm):
    class Meta:
        model = taskFormModel
        fields = ['title','description']