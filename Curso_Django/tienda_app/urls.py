from django.urls import path
from tienda_app import views
#Mostar imagenes



urlpatterns = [

    
   
    path('', views.tienda, name='tienda')
]

