from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description'] #campos que quiero que el formulario tenga - es mejor hacerlo asi que en cada uno de los archivos de la app
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':3})
        } # widgets par el forms son para el diseño de cada uno de los inputs
