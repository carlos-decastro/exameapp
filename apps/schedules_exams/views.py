from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import SchedulingExamForm
from .models import SchedulingExam, Scheduling, Exam, Doctor

# Create your views here.

@login_required(login_url='/contas/login/')
def add_scheduling_exam(request, id_scheduling):
    template_name = 'schedules_exams/add_scheduling_exam.html'
    context = {}
    if request.method == 'POST':
        form = SchedulingExamForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.scheduling = Scheduling.objects.get(id=id_scheduling)
            f.save()
            form.save_m2m()
            return redirect('schedules:list_schedules')
    form = SchedulingExamForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_scheduling_exam(request, id_scheduling_exam):
    schedules_exams = SchedulingExam.objects.get(id=id_scheduling_exam)
    schedules_exams.delete()
    return redirect('schedules:list_schedules')