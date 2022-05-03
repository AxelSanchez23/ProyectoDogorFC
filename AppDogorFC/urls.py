from django.urls import path
from AppDogorFC import views

urlpatterns = [
    path("juntadirectiva/", views.directorio, name= "Directorio"),
    path("jugadores/", views.jugadores, name="Jugadores"),
    path("cuerpotecnico/", views.cuerpotecnico, name="CuerpoTecnico"),
    path("", views.inicio, name="Inicio"),
    path("busquedaJugador", views.busquedaJugador, name="busquedaJugador"),
    path("buscar/", views.buscar),
    ]
