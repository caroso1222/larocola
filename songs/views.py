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


		# rand_song = Song.objects.get(name='La negra tiene tumbao')
		# context['song']=rand_song
		#Calculates the height of the gree box

		
		len_author = len(rand_song.author)
		len_name = len(rand_song.name)

		if len_author > 42 and len_name > 22:
			box_height = 'big_x2'
		elif len_name > 22:
			box_height = 'big_x1'
		elif len_author > 42:
			box_height = 'big_x0'
		else:
			box_height = 'normal'

		context['box_height']=box_height

		return render(request,template,context)
		#output = ', '.join([p.name for p in videos])
	except Exception,err:
		output = ":( ese año no existe"
		print traceback.format_exc()
		return HttpResponse(output)
