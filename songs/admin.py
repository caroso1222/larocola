from django.contrib import admin
from .models import *

# Register your models here.

class YearAdmin(admin.ModelAdmin):
	list_display = ['year']
	class Meta:
		model = Year
		ordering = ['year']

class GenreAdmin(admin.ModelAdmin):
	list_display = ['name']
	class Meta:
		model = Genre
		ordering = ['name']

class SongAdmin(admin.ModelAdmin):
	list_display = ['author','name','youtube_url','year','genre']
	class Meta:
		model = Song
		ordering = ['created']

class VisitorAdmin(admin.ModelAdmin):
	list_display = ['ip','counter_index','counter_years','last_visited','created']

	class Meta:
		model = Visitor

admin.site.register(Song, SongAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Year,YearAdmin)
admin.site.register(Visitor,VisitorAdmin)