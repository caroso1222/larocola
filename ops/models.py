from django.db import models

# Create your models here.
class Evento(models.Model):
	tipoEvento = models.IntegerField(default = 0)
	codigo = models.CharField(max_length = 50, blank = True)
	origen = models.CharField(max_length = 50, blank = True)
	destino = models.CharField(max_length = 50, blank = True)
	fechaSalida = models.DateTimeField(blank = True)
	fechaLlegada = models.DateTimeField(blank = True, null = True)
	fechaSalidaPrevista = models.DateTimeField(blank = True, null = True)
	fechaLlegadaPrevista = models.DateTimeField(blank = True, null = True)
	estadoTripulante = models.CharField(max_length = 50, blank = True)
	estadoVuelo = models.CharField(max_length = 50, blank = True)
	gateSalida = models.CharField(max_length = 20, blank = True)

	def __unicode__(self):
		return ("%s")%self.tipoEvento