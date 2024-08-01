from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def login(request):
    return render(request, 'login.html')


def pacientes(request):
    paciente = Paciente.objects.all()
    return render(request, 'Paciente/index.html', {"pacientes": paciente})


def registrar(request):
    formulario = PacienteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('pacientes')
    return render(request, 'Paciente/registrar.html', {"formulario": formulario})


def editar(request, id):
    paciente = Paciente.objects.get(id=id)
    formulario = PacienteForm(request.POST or None, instance=paciente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('pacientes')
    return render(request, 'Paciente/editar.html', {"formulario": formulario})


def eliminar(request, id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()
    return redirect('pacientes')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}')
            form.save()
    else:
        form = UserCreationForm()
        messages.error(request, 'Error')

    context = {'form': form}
    return render(request, 'login.html', context)
