from django.urls import path
from . import views

app_name='crud'

urlpatterns = [
    path('', views.task_list_and_create, name='crud_list'), #primero indico la url sin nada, despues la lista que se va a cargar cuando acceda a la url, despues le doy nombre a la url
    path('update_task/<int:task_id>', views.update_task, name='update_task'), #en esta url estoy pidiendo que tambien me indique el id de la tarea
    path('edit_task/<int:task_id>', views.edit_task, name='edit_task'), #url para acceder a editar a task
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task')
]