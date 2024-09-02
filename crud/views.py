from django.shortcuts import get_object_or_404, render, redirect
from .models import Task  # permite comunicarnos con la DB
from .forms import TaskForm

# Create your views here.
# Gestionar peticiones http

def task_list_and_create(request):  # la request es obligatoria 
    if request.method == 'POST':
        form = TaskForm(request.POST)  # guardo todo lo que el user me manda desde el formulario
        if form.is_valid():  # valido si la info es valida
            form.save()  # guardo en la base de datos
            return redirect('crud:crud_list')  # para que se recargue automáticamente una vez tocado el botón guardar
    else:
        form = TaskForm()  # Inicializo el formulario en caso de GET

    #tasks = Task.objects.all()


    #distincion entre tareas creadas y no creadas
    completed_tasks = Task.objects.filter(is_completed=True) # pylint: disable=no-member
    incompleted_tasks = Task.objects.filter(is_completed=False) # pylint: disable=no-member



    return render(request, 'task_list.html', {
        'form': form,
        #'tasks': tasks  
        'completed_tasks': completed_tasks,
        'incompleted_tasks': incompleted_tasks # aquí se pasan los queryset de tareas por separado para cada caso (completadas y no completadas)
    })

def update_task(request, task_id): #para actualizar entre tareas completadas y no completadas
    if request.method == 'POST':
        task = Task.objects.get(id=task_id) #pylint: disable= no-member
        task.is_completed = not task.is_completed
        task.save()
        return redirect('crud:crud_list')
    
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id) 
    initial_data = {
        'title': task.title,
        'description': task.description
    }

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('crud:crud_list')
    else:
        form = TaskForm(instance=task, initial=initial_data)
    return render(request, 'edit_task.html', {'form': form})

def delete_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id) #pylint: disable= no-member
        task.delete()
        return redirect('crud:crud_list')