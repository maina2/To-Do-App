from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','due_date','priority','completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
