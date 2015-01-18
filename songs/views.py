# -*- encoding: utf-8 -*-
import traceback
from random import randint
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F

LAST_VIDEOS = 5

def index(request):
	x_forwarded_for = request.META.get('HHTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip_address = x_forwarded_for.split(',')[0]
	else:
		ip_address = request.META.get('REMOTE_ADDR')

	visitor, created = Visitor.objects.get_or_create(ip = ip_address)
	visitor.counter_index = F('counter_index')+1
	visitor.save()
	return render(request, 'index.html')

@csrf_exempt
def videos(request,year):

	if(year!="1960a1979" and year!="1980a1984" and year!="1985a1989" and year!="1990a1994" and 
		year!="1995a1999" and year!="2000a2004" and year!="2005a2009" and year!="2010a2014"):
		output = "Error 404"
		return HttpResponse(output)

	#Increase the counter of videos seen by this user 
	x_forwarded_for = request.META.get('HHTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip_address = x_forwarded_for.split(',')[0]
	else:
		ip_address = request.META.get('REMOTE_ADDR')

	visitor, created = Visitor.objects.get_or_create(ip = ip_address)
	visitor.counter_videos = F('counter_videos')+1
	visitor.save()

	#Saves the previous song in the last_visited FIFO list
	ultimas = visitor.last_visited.split('?')
	if request.method == 'POST':
		previous_song = request.POST.get('previous_song','')
		for i in range(0,LAST_VIDEOS-1):
			ultimas[i]=ultimas[i+1]
		ultimas[LAST_VIDEOS-1]=previous_song
		visitor.last_visited='?'.join(ultimas)
		visitor.save()

	try:
		year_init = int(year.split('a')[0])
		if year_init == 1960:
			songs = Song.objects.filter(year__year__range = [year_init,year_init+19])
		else:
			songs = Song.objects.filter(year__year__range = [year_init,year_init+4])
		count = songs.all().count()

		#Selects a random song that's not in the last_visited list. 
		#This prevents that the next song is one of the last 3 songs.
		stop = False
		while stop != True:
			random_index = randint(0,count-1)
			rand_song = songs[random_index]
			url_code = rand_song.youtube_url.split('=')[1]
			if(url_code!=ultimas[0] and url_code!=ultimas[1] and url_code!=ultimas[2] and url_code!=ultimas[3] and url_code!=ultimas[4]):
				stop = True

		context = {"song": rand_song}
		context['url']=url_code
		template = 'year.html'
		context['year_interval']=year


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
		year_init = int(year.split('a')[0])
		if(year_init>2014):
			output = "Nuestros analistas aún viajan en el DeLorean para traerte la mejor música de %s, espéralo!" %(str(year))
		else:
			output = ":( Estamos trabajando para que puedas escuchar la mejor música de %s, espéralo pronto!" %(str(year))
		print traceback.format_exc()
		return HttpResponse(output)