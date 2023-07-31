from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.forms import PersonaForm, DomicilioForm
from personas.models import Persona, Domicilio
# from django.forms import modelform_factory


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, "personas/detalle.html", {"persona": persona})


def nuevaPersona(request):
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect("inicio")
    else:
        formaPersona = PersonaForm()

    return render(request, "personas/nuevo.html", {"formaPersona": formaPersona})


def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect("inicio")
    else:
        formaPersona = PersonaForm(instance=persona)

    return render(request, "personas/editar.html", {"formaPersona": formaPersona})


def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect("inicio")


def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, "personas/detalle_domicilio.html", {"domicilio": domicilio})


def nuevoDomicilio(request):
    if request.method == "POST":
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect("inicio")
    else:
        formaDomicilio = DomicilioForm()

    return render(request, "personas/nuevo_domicilio.html", {"formaDomicilio": formaDomicilio})


def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == "POST":
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect("inicio")
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)

    return render(request, "personas/editar_domicilio.html", {"formaDomicilio": formaDomicilio})


def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect("inicio")
