import traceback
import sys,os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_song = BASE_DIR + "/csv-files/songs.csv"
django_project_path = BASE_DIR + "/larocola/"

sys.path.append(django_project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.core.wsgi import get_wsgi_application
get_wsgi_application()


from songs.models import *
import csv

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
					song.author = row[0]
					song.name = row[1]
					song.youtube_url = row[2]
					song.year = row[3]
					genre = Genre.objects.get(name=row[4])
					song.genre = genre
					song.save()
			except Exception,err:
				print i
				print "error"
				print traceback.format_exc()
				break
	print "canciones actualizadas"

update_Songs()