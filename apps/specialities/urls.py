from django.urls import path
from . import views

app_name = 'specialities'

urlpatterns = [
    path('', views.list_specialities, name='list_specialities'),
    path('adicionar/', views.add_speciality, name='add_speciality'),
    path('editar/<int:id_speciality>/', views.edit_speciality, name='edit_speciality'),
    path('excluir/<int:id_speciality>/', views.delete_speciality, name='delete_speciality'),
]