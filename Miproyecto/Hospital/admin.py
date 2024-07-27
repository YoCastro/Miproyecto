from django.contrib import admin
from .models import *
# Register your models here.

#admin.site.register(Persona)
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Enfermera)
admin.site.register(Administrador)
admin.site.register(ExpedienteMedico)
admin.site.register(CitaMedica)