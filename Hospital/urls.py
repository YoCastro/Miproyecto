from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('pacientes/registrar/', views.registrar, name='registrar'),
    path('pacientes/editar/', views.editar, name='editar'),
    path('pacientes/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('paciente/<int:pk>/', views.paciente_view, name='paciente_view'),
    path('doctores/', views.doctores, name='doctores'),
    path('doctores/registrar_doc/', views.registrar_doc, name='registrar_doc'),
    path('doctores/editar_doc/', views.editar_doc, name='editar_doc'),
    path('doctores/editar_doc/<int:id>', views.editar_doc, name='editar_doc'),
    path('eliminar_doc/<int:id>', views.eliminar_doc, name='eliminar_doc'),

]