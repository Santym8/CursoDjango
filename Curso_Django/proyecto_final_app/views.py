from django.shortcuts import render



def home(request):

    return render(request,"proyecto_final_app/home.html")


def tienda(request):

    return render(request,"proyecto_final_app/tienda.html")






