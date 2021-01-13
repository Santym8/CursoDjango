from django.urls import path
from servicios_app import views



urlpatterns = [

    
    path('', views.servicios, name='servicios'),
    
]


