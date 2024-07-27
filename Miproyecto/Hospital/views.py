from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def login(request):
    return render(request, 'login.html')

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


def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PacienteForm()
    return render(request, 'registrar_paciente.html', {'form': form})


def registrar_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = DoctorForm()
    return render(request, 'registrar_doctor.html', {'form': form})


def cita_medica(request):
    if request.method == 'POST':
        form = CitaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CitaMedicaForm()
    return render(request, 'Cita_medica.html', {'form': form})
