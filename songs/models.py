from django.db import models

class Year(models.Model):
	year = models.IntegerField(default = 2000)
	clicks = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.year

class Genre(models.Model):
	name = models.CharField(max_length = 50)
	created = models.DateTimeField(auto_now_add = True)
	clicks = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.name

class Song(models.Model):
	author = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	youtube_url = models.URLField()
	year = models.ForeignKey('Year', related_name = 'the_year')
	genre = models.ForeignKey('Genre', related_name = 'genre')
	created = models.DateTimeField(auto_now_add = True)
	clicks = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.name

