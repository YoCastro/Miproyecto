from django.contrib import admin

import Hospital
from .models import *
# Register your models here.

#admin.site.register(Persona)
admin.site.register(Persona)
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Enfermera)
admin.site.register(Administrador)
admin.site.register(ExamenMedico)
admin.site.register(Cita)
admin.site.register(Expediente)
admin.site.register(Medicamento)
admin.site.register(HorarioAtencion)
