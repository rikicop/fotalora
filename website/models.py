from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=500,blank=False)
    def __str__(self):
        template = '{0.name} {0.email} {0.message}'
        return template.format(self)   

