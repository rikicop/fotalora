from django.shortcuts import render
from .models import Contact,Post
from django.http import JsonResponse

def home(request):
    poster=Post.objects.all()
    return render(request, 'home.html', {'poster': poster})


def publicacion(request, pk):
    prod = Post.objects.get(id=pk)
    #context = {'prod':prod}
    return render(request, 'detalle.html', {'prod':prod})