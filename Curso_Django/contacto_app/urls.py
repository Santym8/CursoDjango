from django.urls import path
from contacto_app import views
#Mostar imagenes



urlpatterns = [

    
   
    path('', views.contacto, name='contacto'),

]

