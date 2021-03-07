from django.shortcuts import render
from .models import Contact

def home(request):
    if request.method =="POST":
        name_form = request.POST['namef']
        email_form = request.POST['emailf']
        message_form = request.POST['messagef']
        #Insertar el objeto
        Contact.objects.create(name=name_form,email=email_form,message=message_form)

        return render(request, 'home.html', {})
          
    else:
        
        return render(request, 'home.html',{})

    return render(request, 'home.html', {})
