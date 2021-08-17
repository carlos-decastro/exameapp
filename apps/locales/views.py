from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import LocaleForm
from .models import Locale

# Create your views here.

@login_required(login_url='/contas/login/')
def add_locale(request):
    template_name = 'locales/add_locale.html'
    context = {}
    if request.method == 'POST':
        form = LocaleForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('locales:list_locales')
    form = LocaleForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_locales(request):
    template_name = 'locales/list_locales.html'
    locales = Locale.objects.filter()
    context = {
        'locales': locales
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_locale(request, id_locale):
    template_name = 'locales/add_locale.html'
    context ={}
    locale = get_object_or_404(Locale, id=id_locale)
    if request.method == 'POST':
        form = LocaleForm(request.POST, instance=locale)
        if form.is_valid():
            form.save()
            return redirect('locales:list_locales')
    form = LocaleForm(instance=locale)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_locale(request, id_locale):
    locale = Locale.objects.get(id=id_locale)
    locale.delete()
    return redirect('locales:list_locales')


