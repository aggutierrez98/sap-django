from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona, Domicilio


def bienvenido(request):
    no_personas = Persona.objects.count()
    no_domicilios = Domicilio.objects.count()
    #personas = Persona.objects.all()
    #domicilios = Domicilio.objects.all()
    personas = Persona.objects.order_by("id")
    domicilios = Domicilio.objects.order_by("id")
    return render(request, "bienvenido.html", {"no_personas": no_personas, "personas": personas, "no_domicilios": no_domicilios, "domicilios": domicilios})



