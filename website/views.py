from django.shortcuts import render
from .models import Contact
from django.http import JsonResponse

def home(request):
    if request.method =="POST":
        name_form = request.POST['namef']
        email_form = request.POST['emailf']
        message_form = request.POST['messagef']
        #Insertar el objeto
        Contact.objects.create(name=name_form,email=email_form,message=message_form)
         
        return JsonResponse({"name_form":name_form}, status=200) 
        return render(request, 'home.html', {"name_form":name_form})
          
    else:
        
        return render(request, 'home.html',{})

    return render(request, 'home.html', {})
