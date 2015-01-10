from django.db import models

# Create your models here.
class Song(models.Model):
	author = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	youtube_url = models.URLField()
	year = models.IntegerField(default = 2000)
	genre = models.ForeignKey('Genre', related_name = 'genre')
	created = models.DateTimeField(auto_now_add = True)

class Genre(models.Model):
	name = models.CharField(max_length = 50)
	created = models.DateTimeField(auto_now_add = True)