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

]