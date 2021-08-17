from django.urls import path
from . import views

app_name = 'schedules_exams'

urlpatterns = [
    path('adicionar/<int:id_scheduling>/', views.add_scheduling_exam, name='add_scheduling_exam'),
    path('excluir/<int:id_scheduling_exam>/', views.delete_scheduling_exam, name='delete_scheduling_exam'),
]