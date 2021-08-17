"""ExameApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static #Não tem no manual
from django.conf import settings #Não tem no manual

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('pacientes/', include('patients.urls', namespace='patients')),
    path('especialidades/', include('specialities.urls', namespace='specialities')),
    path('doutores/', include('doctors.urls', namespace='doctors')),
    path('locais/', include('locales.urls', namespace='locales')),
    path('agendas/', include('schedules.urls', namespace='schedules')),
    path('exames/', include('exams.urls', namespace='exams')),
    path('AgendasExames/', include('schedules_exams.urls', namespace='schedules_exams')),
    path('contas/', include('accounts.urls', namespace='accounts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)