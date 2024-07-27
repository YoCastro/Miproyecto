from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)


class Paciente(Persona):
    numero_historia_clinica = models.CharField(max_length=50)
    enfermedades = models.TextField()

    def __str__(self):
        return f'{self.id} {self.nombre} {self.apellido}'

    def actualizar_datos(self, nombre=None, apellido=None, fecha_nacimiento=None, direccion=None, telefono=None, email=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if fecha_nacimiento:
            self.fecha_nacimiento = fecha_nacimiento
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono
        if email:
            self.email = email
        self.save()

class Doctor(Persona):
    numero_licencia = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f'Dr. {self.nombre} {self.apellido}'

    def actualizar_datos(self, nombre=None, apellido=None, especialidad=None, telefono=None, email=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if especialidad:
            self.especialidad = especialidad
        if telefono:
            self.telefono = telefono
        if email:
            self.email = email
        self.save()

class Enfermera(Persona):
    numero_licencia = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def actualizar_datos(self, nombre=None, apellido=None, especialidad=None, turno=None, telefono=None, email=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if especialidad:
            self.especialidad = especialidad
        if turno:
            self.turno = turno
        if telefono:
            self.telefono = telefono
        if email:
            self.email = email
        self.save()

class Administrador(Persona):
    id_empleado = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.rol}'

    def actualizar_datos(self, nombre=None, apellido=None, telefono=None, email=None, rol=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if telefono:
            self.telefono = telefono
        if email:
            self.email = email
        if rol:
            self.rol = rol
        self.save()

class ExpedienteMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    historial_clinico = models.TextField()
    enfermedad = models.TextField(blank=True, null=True)
    medicamentos = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Expediente de {self.paciente}'

    def actualizar_historial(self, historial_clinico):
        self.historial_clinico = historial_clinico
        self.save()

    def agregar_enfermedad(self, enfermedad):
        self.enfermedad += f', {enfermedad}'
        self.save()

    def agregar_medicamento(self, medicamento):
        self.medicamentos += f', {medicamento}'
        self.save()

class CitaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Cita de {self.paciente} con {self.medico} el {self.fecha} a las {self.hora}'

    def programar_cita(self, fecha, hora, motivo):
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.save()

    def cancelar_cita(self):
        self.delete()

    def actualizar_notas(self, notas):
        self.notas = notas
        self.save()