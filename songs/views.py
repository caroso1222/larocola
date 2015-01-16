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
	visitor.counter_index = F('counter_index')+1
	visitor.save()
	return render(request, 'index.html')

@csrf_exempt
def videos(request,year):

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
		ultimas[0]=ultimas[1]
		ultimas[1]=ultimas[2]
		ultimas[2]=previous_song
		visitor.last_visited='?'.join(ultimas)
		visitor.save()
		print visitor.last_visited

	try:
		songs = Song.objects.filter(year__year = year)
		count = songs.all().count()

		#Selects a random song that's not in the last_visited list. 
		#This prevents that the next song is one of the last 3 songs.
		stop = False
		while stop != True:
			random_index = randint(0,count-1)
			rand_song = songs[random_index]
			url_code = rand_song.youtube_url.split('=')[1]
			if(url_code!=ultimas[0] and url_code!=ultimas[1] and url_code!=ultimas[2]):
				stop = True

		context = {"song": rand_song}
		#url_init = "//www.youtube.com/embed/"
		#autoplay = "?autoplay=1"
		#final_url = url_init+url_code+autoplay
		context['url']=url_code
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
		if(int(year)>2014):
			output = "Nuestros analistas aún viajan en el DeLorean para traerte la mejor música de %s, espéralo!" %(str(year))
		else:
			output = ":( Estamos trabajando para que puedas escuchar la mejor música de %s, espéralo pronto!" %(str(year))
		print traceback.format_exc()
		return HttpResponse(output)