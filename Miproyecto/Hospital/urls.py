from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('registrar_paciente/', views.registrar_paciente, name='registrar_paciente'),
    path('registrar_doctor/', views.registrar_doctor, name='registrar_doctor'),
    path('cita_medica/', views.cita_medica, name='Cita_Medica'),
]