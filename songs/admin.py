from django.contrib import admin
from .models import *

# Register your models here.
class SongAdmin(admin.ModelAdmin):
	list_display = ['author','name','youtube_url','year','genre']
	class Meta:
		model = Song
		ordering = ['created']

class GenreAdmin(admin.ModelAdmin):
	list_display = ['name']
	class Meta:
		model = Genre
		ordering = ['name']

admin.site.register(Song, SongAdmin)
admin.site.register(Genre,GenreAdmin)