from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import DoctorForm
from .models import Doctor, Speciality, DoctorSpeciality



# Create your views here.

@login_required(login_url='/contas/login/')
def add_doctor(request):
    template_name = 'doctors/add_doctor.html'
    context = {}
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('doctors:list_doctors')
    form = DoctorForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_doctors(request):
    template_name = 'doctors/list_doctors.html'
    doctors = Doctor.objects.filter()
    specialities = Speciality.objects.filter()
    doctors_specialities = DoctorSpeciality.objects.filter()
    context = {
        'doctors': doctors,
        'specialities': specialities,
        'doctors_specialities': doctors_specialities,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_doctor(request, id_doctor):
    template_name = 'doctors/add_doctor.html'
    context ={}
    doctor = get_object_or_404(Doctor, id=id_doctor)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors:list_doctors')
    form = DoctorForm(instance=doctor)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_doctor(request, id_doctor):
    doctor = Doctor.objects.get(id=id_doctor)
    doctor.delete()
    return redirect('doctors:list_doctors')
