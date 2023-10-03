from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {'tittle', 'description', 'important'}
        widget = {
            'tittle': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Write a tittle'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Write a description'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-control'
                                                    'text-center m-auto'})
        }