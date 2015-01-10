from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
	output = 'hola'
	return HttpResponse(output)

def videos(request,year):
	output = 'hola'
	return HttpResponse(output)

