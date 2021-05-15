from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=500,blank=False)
    def __str__(self):
        template = '{0.name} {0.email} {0.message}'
        return template.format(self)

class Post(models.Model):
    titulo = models.CharField(max_length=100,blank=False)
    autor = models.CharField(max_length=100,blank=False)
    contenido = models.TextField(max_length=500,blank=False)
    img = models.FileField(blank=True, null=True)
    def __str__(self):
        template = '{0.titulo} {0.autor}'
        return template.format(self)

class PostList(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    lista = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.post.titulo     

