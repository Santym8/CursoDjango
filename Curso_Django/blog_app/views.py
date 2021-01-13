from typing import cast
from django.shortcuts import render
from blog_app.models import Post, Categoria

# Create your views here.
def blog(request):

    
    posts=Post.objects.all()
    
    categorias=Categoria.objects.all()

    categorias_mostrar=[]
    for categoria in categorias:
        categorias_mostrar.append(categoria)
    
    set(categorias_mostrar)
    



    return render(request,"blog/blog.html", {
        'posts':posts,
        'categorias':categorias_mostrar
        })


def categoria(request, categoria_id):
    
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)


    return render(request, 'blog/categorias.html', {
        'categoria':categoria,
        'posts':posts
    } )
    