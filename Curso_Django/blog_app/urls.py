from django.urls import path
from blog_app import views
#Mostar imagenes



urlpatterns = [


    path('', views.blog, name='blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    
]

