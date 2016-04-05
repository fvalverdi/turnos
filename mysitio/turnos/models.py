from django.db import models

class Personas (models.Model):
	apellido = models.CharField(max_length=50)
	nombres = models.CharField(max_length=100)
	fecha_nac = models.DateField('Fecha de nacimiento')
	domicilio = models.CharField(max_length=200)
	telefono = models.CharField(max_length=15)
	dni = models.IntegerField()
	sexo = models.CharField(max_length=1)

	def __str__(self):
            return self.nombres

class Especialidades (models.Model):
	nombre = models.CharField(max_length=100)
	mat_especialidad = models.IntegerField()

	def __str__(self):
            return self.nombre
		
class Medicos (Personas):
	mat_profesional = models.IntegerField()
	#persona = models.ForeignKey (Personas)
	especialidad = models.ForeignKey(Especialidades)

	#def __str__(self):
     #       return self.mat_profesional

class Pacientes (Personas):
	#persona = models.ForeignKey(Personas)
	fecha_inicio = models.DateField('Fecha de Alta Como paciente')
	altura = models.IntegerField()
	peso = models.IntegerField()
	perimetro_enc = models.IntegerField()

	def __str__(self):
            return self.nombres
	
class Historias_medicas (models.Model):
	paciente = models.ForeignKey(Pacientes)
	medico = models.ForeignKey(Medicos)
	fecha_historia = models.DateTimeField('Fecha de Creacion')
	diagnostico = models.CharField(max_length=500)
	tratamiento = models.CharField(max_length=500)

	def __str__(self):
            return self.paciente.nombres

class Organizacion (models.Model):
	nombre = models.CharField(max_length=100)
	domicilio = models.CharField(max_length=200)
	telefono = models.CharField(max_length=15)

	def __str__(self):
            return self.nombre

class Tipo_Usuario (models.Model):
	nombre = models.CharField(max_length=20)

	def __str__(self):
            return self.nombre

class Usuarios (models.Model):
	persona = models.ForeignKey(Personas)
	tipo_usuario = models.ForeignKey (Tipo_Usuario)
	organizacion = models.ForeignKey(Organizacion)

	def __str__(self):
            return self.persona.nombres
		
class Turnos (models.Model):
	medico = models.ForeignKey(Medicos)
	paciente = models.ForeignKey(Pacientes)
	usuario = models.ForeignKey(Usuarios)
	fecha = models.DateTimeField('Fecha del Turno')
	organizacion = models.ForeignKey(Organizacion)

	def __str__(self):
            return self.paciente.nombres


	


		
# Create your models here.
#	class Pregunta(models.Model):
#		texto_pregunta = models.CharField(max_length=200)
#		fecha = models.DateTimeField(‘Fecha de publicación’)
#	class Opcion(models.Model):
#		pregunta = models.ForeignKey(Pregunta)
#		texto_opcion = models.CharField(max_length=200)
#		votos = models.IntegerField(default=0)