from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from datetime import datetime
from django.template import RequestContext

VUELO = 1
RESERVA = 2
LIBRE = 3
VACIO = 4
OTRO = 5

# Create your views here.
@csrf_exempt
def addEvento(request):
	#Evento.objects.all().delete()
	if request.method == "POST":
		vueloStr = "%d"%VUELO
		libreStr = "%d"%LIBRE
		reservaStr = "%d"%RESERVA

		fechaSalida = datetime(int(request.POST['anhoSalida']),int(request.POST['mesSalida']),int(
				request.POST['diaSalida']),int(request.POST['horaSalida']),int(request.POST['minutoSalida']),0)

		if request.POST['tipoEvento'] == vueloStr: #es un vuelo el que llega
			fechaLlegada = datetime(int(request.POST['anhoLlegada']),int(request.POST['mesLlegada']),int(
				request.POST['diaLlegada']),int(request.POST['horaLlegada']),int(request.POST['minutoLlegada']),0)
			fechaSalidaPrevista = datetime(int(request.POST['anhoSalidaPrevista']),int(request.POST['mesSalidaPrevista']),int(
				request.POST['diaSalidaPrevista']),int(request.POST['horaSalidaPrevista']),int(request.POST['minutoSalidaPrevista']),0)
			fechaLlegadaPrevista = datetime(int(request.POST['anhoLlegadaPrevista']),int(request.POST['mesLlegadaPrevista']),int(
				request.POST['diaLlegadaPrevista']),int(request.POST['horaLlegadaPrevista']),int(request.POST['minutoLlegadaPrevista']),0)

			if request.POST['gateSalida'] != "":
				gateSalida = request.POST['gateSalida']
			else:
				gateSalida = "N/A"

			evento = Evento(
				tipoEvento = VUELO,
				codigo = request.POST['codigoVuelo'],
				origen = request.POST['origen'],
				destino = request.POST['destino'],
				fechaSalida = fechaSalida,
				fechaLlegada = fechaLlegada,
				fechaSalidaPrevista = fechaSalidaPrevista,
				fechaLlegadaPrevista = fechaLlegadaPrevista,
				estadoTripulante = request.POST['estadoTripulante'],
				estadoVuelo = request.POST['estadoVuelo'],
				gateSalida = gateSalida,
				)
			evento.save()
		elif request.POST['tipoEvento'] == libreStr:
			evento = Evento(
				tipoEvento = LIBRE,
				fechaSalida = fechaSalida,
				estadoTripulante = request.POST['estadoTripulante'],
				)
			evento.save()
		elif request.POST['tipoEvento'] == reservaStr:
			evento = Evento(
				tipoEvento = RESERVA,
				fechaSalida = fechaSalida,
				estadoTripulante = request.POST['estadoTripulante'],
				)
			evento.save()

		html = "<html><body>It is now %s.</body></html>" % "muaha"
		return HttpResponse(html)
	else:
		mifecha = datetime.now()
		mifecha = datetime(2014,12,10,20,30,20)
		print mifecha.year
		html = "<html><body>It is now %d.</body></html>" % mifecha.minute
		return HttpResponse(html)

def verItinerario(request):
	mydict = {}
	mydict['listas'] = {}
	nombres =[] 
	for i in range(1,31):
		eventos = Evento.objects.filter(fechaSalida__day=i)
		elnombre = "eventos%d"%i
		mydict['listas'][elnombre] = eventos
		nombres.append(elnombre)
	mydict['nombres'] = nombres
	return render_to_response('ops_summary.html', mydict, context_instance=RequestContext(request))
	#return render(request,'ops_summary.html', context)



