# -*- encoding: utf-8 -*-
import traceback
import sys,os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_song = BASE_DIR + "/csv-files/songs.csv"
csv_genre = BASE_DIR + "/csv-files/genres.csv"
csv_year = BASE_DIR + "/csv-files/years.csv"
django_project_path = BASE_DIR + "/larocola/"

sys.path.append(django_project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.core.wsgi import get_wsgi_application
get_wsgi_application()


from songs.models import *
import csv

def update_Years():
	Year.objects.all().delete() # Se borran todos los registros de la tabla
	with open(csv_year,'rb') as csv_file:
		data_reader = csv.reader(csv_file.read().splitlines())
		i = 0
		for row in data_reader:
			i = i+1
			try:
				if row[0]!='anho': # No se mete el primer registro
					anho = Year()
					anho.year = row[0].strip()
					anho.save()
			except Exception,err:
				print i
				print "error"
				print traceback.format_exc()
				break
	print "años actualizados"

def update_Genres():
	Genre.objects.all().delete() # Se borran todos los registros de la tabla
	with open(csv_genre,'rb') as csv_file:
		data_reader = csv.reader(csv_file.read().splitlines())
		i = 0
		for row in data_reader:
			i = i+1
			try:
				if row[0]!='generos': # No se mete el primer registro
					genre = Genre()
					genre.name = row[0].strip()
					genre.save()
			except Exception,err:
				print i
				print "error"
				print traceback.format_exc()
				break
	print "generos actualizados"

def update_Songs():
	Song.objects.all().delete() # Se borran todos los registros de la tabla
	with open(csv_song,'rb') as csv_file:
		data_reader = csv.reader(csv_file.read().decode("latin1").encode('utf8').splitlines())
		i = 0
		for row in data_reader:
			i = i+1
			try:
				if row[0]!='autor': # No se mete el primer registro
					song = Song()
					song.author = row[0].strip()
					song.name = row[1].strip()
					song.youtube_url = row[2].strip()
					year = Year.objects.get(year=row[3].strip())
					song.year = year
					genre = Genre.objects.get(name=row[4].strip())
					song.genre = genre
					song.save()
			except Exception,err:
				print i
				print "error"
				print row[4]
				print traceback.format_exc()
				break
	print "canciones actualizadas"

update_Years()
update_Genres()
update_Songs()