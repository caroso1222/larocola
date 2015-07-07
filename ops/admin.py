from django.contrib import admin
from .models import *
from ops import views
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
	list_display = ['getTipoEvento','codigo','origen','destino','fechaSalida','fechaLlegada','fechaSalidaPrevista','fechaLlegadaPrevista','estadoTripulante','estadoVuelo','gateSalida']

	def getTipoEvento(self,obj):
		if obj.tipoEvento == views.VUELO:
			return "Vuelo"
		elif obj.tipoEvento == views.RESERVA:
			return "Reserva"
		elif obj.tipoEvento == views.LIBRE:
			return "Libre"
		else:
			return "Vacio"

	getTipoEvento.short_description = 'tipoEvento'
	getTipoEvento.admin_order_field = 'tipoEvento'

	class Meta:
		model = Evento
		ordering = ['fechaSalida']

admin.site.register(Evento, EventoAdmin)

