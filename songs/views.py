# -*- encoding: utf-8 -*-
import traceback
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
	return render(request, 'index.html')

def videos(request,year):
	try:
		videos = Song.objects.filter(year__year = year)
		output = ', '.join([p.name for p in videos])
	except Exception,err:
		output = ":( ese año no existe"
	return render(request, 'year.html')
	#return HttpResponse(output)

