from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('', views.list_doctors, name='list_doctors'),
    path('adicionar/', views.add_doctor, name='add_doctor'),
    path('editar/<int:id_doctor>/', views.edit_doctor, name='edit_doctor'),
    path('excluir/<int:id_doctor>/', views.delete_doctor, name='delete_doctor'),
]