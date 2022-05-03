import email
from django.http import HttpResponse
from django.shortcuts import render
from AppDogorFC.models import jugadores


# Create your views here.

def directorio(request):

    return render (request, "AppDogorFC/juntadirectiva.html")

def jugadores(request):

    return render (request, "AppDogorFC/jugadores.html")    

def cuerpotecnico(request):

    return render(request, "AppDogorFC/cuerpotecnico.html")

def inicio(request):
    
    return render (request, "AppDogorFC/inicio.html")

def busquedaJugador(request):

    return render(request, "AppDogorFC/busquedaJugador.html")

def buscar(request):
    if request.GET["jugador"]:
        jugador = request.GET["jugador"]
        jugadoRESS = jugadores.objects.filter(jugador__icontains=jugador)

        return render (request, "AppDogorFC/resultadosBusquedas.html", {"jugadores":jugador, "jugadoRESS":jugadoRESS })

    else:
        respuesta = "No enviaste datos"

        return HttpResponse(respuesta)

  
