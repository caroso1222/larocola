# -*- encoding: utf-8 -*-
import traceback
from random import randint
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F

def index(request):
	x_forwarded_for = request.META.get('HHTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip_address = x_forwarded_for.split(',')[0]
	else:
		ip_address = request.META.get('REMOTE_ADDR')

	visitor, created = Visitor.objects.get_or_create(ip = ip_address)
	visitor.counter = F('counter_index')+1
	visitor.save()
	return render(request, 'index.html')

@csrf_exempt
def videos(request,year):
	try:
		songs = Song.objects.filter(year__year = year)
		count = songs.all().count()
		random_index = randint(0,count-1)
		rand_song = songs[random_index]

		context = {"song": rand_song}
		url_code = rand_song.youtube_url.split('=')[1]
		#url_init = "//www.youtube.com/embed/"
		#autoplay = "?autoplay=1"
		#final_url = url_init+url_code+autoplay
		print url_code
		context['url']=url_code
		context['year']=year
		template = 'year.html'


		# rand_song = Song.objects.get(name='La negra tiene tumbao')
		# context['song']=rand_song
		#Calculates the height of the gree box

		
		len_author = len(rand_song.author)
		len_name = len(rand_song.name)

		if len_author > 42 and len_name > 20:
			box_height = 'big_x2'
		elif len_name > 20:
			box_height = 'big_x1'
		elif len_author > 42:
			box_height = 'big_x0'
		else:
			box_height = 'normal'

		context['box_height']=box_height

		return render(request,template,context)
		#output = ', '.join([p.name for p in videos])
	except Exception,err:
		output = ":( Estamos trabajando para que puedas escuchar la mejor música de este año, espéralo pronto."
		print traceback.format_exc()
		return HttpResponse(output)