from django.conf.urls import url
from ops import views

urlpatterns = [
    url(r'^add/', views.addEvento, name='add_evento'),
    url(r'^ver/', views.verItinerario, name='ver_itinerario'),
]