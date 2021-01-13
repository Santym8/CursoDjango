from django.shortcuts import render

from servicios_app.models import Servicio

# Create your views here.
def servicios(request):
    serv=Servicio.objects.all()
    return render(request,"servicios/servicios.html", {'servicios':serv})
    