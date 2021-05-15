from django.shortcuts import render, get_object_or_404
from .models import Contact,Post,PostList
#from django.http import JsonResponse

def home(request):
    poster=Post.objects.all()
    return render(request, 'home.html', {'poster': poster})


def publicacion(request, pk):
    prod = Post.objects.get(id=pk)
    
    #Para la Lista
    post = get_object_or_404(Post, id=pk)
    lista = PostList.objects.filter(post=post)
    
    #context = {'prod':prod}
    return render(request, 'detalle.html', {'prod':prod, 'post':post, 'lista': lista })