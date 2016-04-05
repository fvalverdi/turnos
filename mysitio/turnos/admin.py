from django.contrib import admin

from .models import *

admin.site.register(Personas)
admin.site.register(Tipo_Usuario)
admin.site.register(Especialidades)
admin.site.register(Medicos)
admin.site.register(Pacientes)
admin.site.register(Historias_medicas)
admin.site.register(Organizacion)
admin.site.register(Usuarios)
admin.site.register(Turnos)


# Register your models here.
