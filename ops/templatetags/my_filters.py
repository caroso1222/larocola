from django import template

register = template.Library()

def key(dictionary, key_name):
	elnombre = "eventos%d"%key_name
	return dictionary.get(elnombre)
key = register.filter('key', key)
