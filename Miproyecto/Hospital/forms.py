from django import forms
from .models import *

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class EnfermeraForm(forms.ModelForm):
    class Meta:
        model = Enfermera
        fields = '__all__'

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'

class ExamenForm(forms.ModelForm):
    class Meta:
        model: ExamenMedico
        fields = '__all__'

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model: Expediente
        fields = '__all__'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model: Medicamento
        fields = '__all__'

class HorarioForm(forms.ModelForm):
    class Meta:
        model: HorarioAtencion
        fields = '__all__'