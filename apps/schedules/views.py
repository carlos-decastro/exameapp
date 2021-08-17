from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import SchedulingForm
from .models import Scheduling, Patient, Locale 
from schedules_exams.models import SchedulingExam
from exams.models import Exam
from doctors.models import Doctor, Speciality, DoctorSpeciality
from apps import schedules


# Create your views here.

@login_required(login_url='/contas/login/')
def add_scheduling(request, id_patient):
    template_name = 'schedules/add_scheduling.html'
    context = {}
    if request.method == 'POST':
        form = SchedulingForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.patient = Patient.objects.get(id=id_patient)
            f.save()
            form.save_m2m()
            return redirect('schedules:list_schedules')
    form = SchedulingForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_schedules(request):
    template_name = 'schedules/list_schedules.html'
    patients = Patient.objects.filter()
    locales = Locale.objects.filter()
    schedules = Scheduling.objects.filter()
    schedules_exams = SchedulingExam.objects.filter()
    exams = Exam.objects.filter()
    doctors = Doctor.objects.filter()
    doctors_specialities = DoctorSpeciality.objects.filter()
    specialities = Speciality.objects.filter()
    context = {
        'patients': patients,
        'locales': locales,
        'schedules': schedules,
        'schedules_exams' : schedules_exams,
        'exams' : exams,
        'doctors' : doctors,
        'specialities': specialities,
        'doctors_specialities': doctors_specialities,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_scheduling(request, id_scheduling):
    template_name = 'schedules/add_scheduling.html'
    context ={}
    scheduling = get_object_or_404(Scheduling, id=id_scheduling)
    if request.method == 'POST':
        form = SchedulingForm(request.POST, instance=scheduling)
        if form.is_valid():
            form.save()
            return redirect('schedules:list_schedules')
    form = SchedulingForm(instance=scheduling)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_scheduling(request, id_scheduling):
    scheduling = Scheduling.objects.get(id=id_scheduling)
    scheduling.delete()
    return redirect('schedules:list_schedules')

@login_required(login_url='/contas/login/')
def edit_scheduling_status(request, id_scheduling):
    template_name = 'schedules/edit_scheduling_status.html'
    context ={}
    scheduling = get_object_or_404(Scheduling, id=id_scheduling)
    if request.method == 'POST':
        form = SchedulingForm(request.POST, instance=scheduling)
        if form.is_valid():
            form.save()
            return redirect('Schedules:list_schedules')
    form = SchedulingForm(instance=scheduling)
    context['form'] = form
    return render(request, template_name, context)    
