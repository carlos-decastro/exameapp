from apps import specialities
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import SpecialityForm
from .models import Speciality

# Create your views here.

@login_required(login_url='/contas/login/')
def add_speciality(request):
    template_name = 'specialities/add_speciality.html'
    context = {}
    if request.method == 'POST':
        form = SpecialityForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('specialities:list_specialities')
    form = SpecialityForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_specialities(request):
    template_name = 'specialities/list_specialities.html'
    specialities = Speciality.objects.filter()
    context = {
        'specialities': specialities
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_speciality(request, id_speciality):
    template_name = 'specialities/add_speciality.html'
    context ={}
    speciality = get_object_or_404(Speciality, id=id_speciality)
    if request.method == 'POST':
        form = SpecialityForm(request.POST, instance=speciality)
        if form.is_valid():
            form.save()
            return redirect('specialities:list_specialities')
    form = SpecialityForm(instance=speciality)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_speciality(request, id_speciality):
    speciality = Speciality.objects.get(id=id_speciality)
    speciality.delete()
    return redirect('specialities:list_specialities')
