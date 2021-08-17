
from django.urls import path
from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.list_schedules, name='list_schedules'),
    path('adicionar/<int:id_patient>/', views.add_scheduling, name='add_scheduling'),
    path('editar/<int:id_scheduling>/', views.edit_scheduling, name='edit_scheduling'),
    path('excluir/<int:id_scheduling>/', views.delete_scheduling, name='delete_scheduling'),
    path('editar-status/<int:id_scheduling>/', views.edit_scheduling_status, name='edit_scheduling_status'),
]