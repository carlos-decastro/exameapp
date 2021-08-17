from django.urls import path
from . import views

app_name = 'locales'

urlpatterns = [
    path('', views.list_locales, name='list_locales'),
    path('adicionar/', views.add_locale, name='add_locale'),
    path('editar/<int:id_locale>/', views.edit_locale, name='edit_locale'),
    path('excluir/<int:id_locale>/', views.delete_locale, name='delete_locale'),
]