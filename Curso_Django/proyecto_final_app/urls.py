
from django.urls import path
from proyecto_final_app import views
#Mostar imagenes



urlpatterns = [

    path('', views.home,name='home'),
    
  

]

