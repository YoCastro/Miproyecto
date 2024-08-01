from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido", blank=True, null=True)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255, verbose_name="Direccion")
    telefono = models.CharField(max_length=20, verbose_name="Telefono")

    def __str__(self):
        return self.nombre

class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    dosis = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class ExamenMedico(models.Model):
    id_examen = models.AutoField(primary_key=True)
    fecha = models.DateField()
    tipo_de_examen = models.CharField(max_length=100)
    resultado = models.TextField()
    costo = models.FloatField()

    def agendar_examen(self, paciente, fecha, tipo_de_examen, costo):
        self.paciente = paciente
        self.fecha = fecha
        self.tipo_de_examen = tipo_de_examen
        self.costo = costo
        self.save()

    def __str__(self):
        return f"{self.tipo_de_examen} - {self.paciente.nombre}"

class Expediente(models.Model):
    id_expediente = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    historial_medico = models.TextField()
    notas_medicas = models.TextField(blank=True, null=True)
    examenes_medicos = models.ManyToManyField(ExamenMedico, related_name='expedientes')

    def agregar_nota_medica(self, nota):
        if self.notas_medicas:
            self.notas_medicas += f"\n{nota}"
        else:
            self.notas_medicas = nota
        self.save()

    def agregar_enfermedad(self, enfermedad):
        self.enfermedad += f', {enfermedad}'
        self.save()

    def agregar_medicamento(self, medicamento):
        self.medicamentos += f', {medicamento}'
        self.save()

    def __str__(self):
        return f"Expediente {self.id_expediente} - {self.fecha_creacion}"

class Paciente(Persona):
    expedientes = models.ForeignKey(Expediente, on_delete=models.CASCADE, related_name='pacientes', default=None)
    historial_medicamentos = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='pacientes', default=None)
    contacto_emergencia = models.CharField(max_length=20, verbose_name="Contacto de Emergencia", blank=True, null=True)

    def consultar_expediente(self):
        return self.expedientes.all()

    def actualizar_contacto_emergencia(self, nuevo_contacto):
        self.contacto_emergencia = nuevo_contacto
        self.save()

    def agendar_cita(self, cita):
        if isinstance(cita, Cita):
            cita.paciente = self
            cita.save()
        else:
            raise ValidationError("Objeto cita no válido")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class HorarioAtencion(models.Model):
    id = models.AutoField(primary_key=True)
    dia_semana = models.CharField(max_length=15)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    disponible_para_citas = models.BooleanField(default=True)

    def es_horario_disponible(self, hora):
        if self.hora_inicio <= hora <= self.hora_fin:
            return self.disponible_para_citas
        return False

    def agendar_cita(self, paciente, fecha, hora):
        if self.es_horario_disponible(hora):
            cita = Cita(paciente=paciente, fecha=fecha, hora=hora, doctor=self.doctores, motivo="Consulta médica")
            cita.save()
            return cita
        else:
            raise ValidationError("Horario no disponible")

    def __str__(self):
        return f"{self.dia_semana}: {self.hora_inicio} - {self.hora_fin}"

class Doctor(Persona):
    numero_licencia = models.CharField(max_length=50,null=True, default='')
    especialidad = models.CharField(max_length=100)
    horario = models.ForeignKey(HorarioAtencion, on_delete=models.CASCADE, related_name='doctores', default=1, null=True)

    def agendar_cita(self, paciente, fecha, hora, motivo):
        cita = Cita.objects.create(
            paciente=paciente,
            fecha=fecha,
            hora=hora,
            motivo=motivo,
            doctor=self,
            estado='Programada'
        )
        return cita

    def consultar_pacientes(self):
        return Paciente.objects.filter(citas__doctor=self).distinct()

    def __str__(self):
        return f"Dr. {self.nombre} - Especialidad: {self.especialidad}"


# Modelo de Enfermera
class Enfermera(Persona):
    licencia = models.CharField(max_length=50, null=True, default='')
    area_de_asignacion = models.CharField(max_length=100, default='General')
    turno = models.ForeignKey(HorarioAtencion, on_delete=models.CASCADE, related_name='enfermeras', default=1, null=True)

    def __str__(self):
        return f"Enfermera {self.nombre} - Área: {self.area_de_asignacion}"


class Administrador(Persona):
    id_empleado = models.AutoField(primary_key=True)
    tipo_de_personal = models.CharField(max_length=50, choices=[
        ('Doctor', 'Doctor'),
        ('Enfermera', 'Enfermera'),
    ], default='Doctor')

    def registrar_doctor(self, doctor):
        if isinstance(doctor, Doctor):
            doctor.save()
        else:
            raise ValidationError("Objeto de personal de salud no válido")

    def registrar_enfermera(self, enfermera):
        if isinstance(enfermera, Enfermera):
            enfermera.save()
        else:
            raise ValidationError("Objeto de personal de salud no válido")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, default='Pendiente')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='citas')

    def programar_cita(self, fecha, hora, motivo, paciente, doctor):
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.paciente = paciente
        self.doctor = doctor
        self.estado = 'Programada'
        self.save()

    def cancelar_cita(self):
        self.estado = 'Cancelada'
        self.save()

    def __str__(self):
        return f"Cita con Dr. {self.doctor.nombre} - {self.fecha}"




