from django.contrib import admin
from .models import Task #importo el modelo
# Register your models here.

@admin.register(Task) #registro el modelo Task

class Taskadmin(admin.ModelAdmin):
    list_display = ['title', 'is_completed']