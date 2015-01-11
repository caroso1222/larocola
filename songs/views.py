# -*- encoding: utf-8 -*-
import traceback
from random import randint
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
	return render(request, 'index.html')

def videos(request,year):
	try:
		songs = Song.objects.filter(year__year = year)
		count = songs.all().count()
		random_index = randint(0,count-1)
		rand_song = songs[random_index]
		context = {"song": rand_song}
		url_code = rand_song.youtube_url.split('=')[1]
		url_init = "//www.youtube.com/embed/"
		autoplay = "?autoplay=1"
		final_url = url_init+url_code+autoplay
		print final_url
		context['url']=final_url
		template = 'year.html'
		return render(request,template,context)
		#output = ', '.join([p.name for p in videos])
	except Exception,err:
		output = ":( ese año no existe"
		return HttpResponse(output)

