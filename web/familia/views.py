from django.shortcuts import render
from django.http import HttpResponse
from familia.models import Integrante

# Create your views here.

def bienvenida(request):
 #   return HttpResponse('Bienvenido a Data-Family')
    context ={ }

    return render(request, '01_saludo.html',context=context)


def create_member(request):
   
   new_member = Integrante.objects.create( name = 'Jorge Ríos', 
                                           date_of_birth = '24/12/76' ,
                                           age = 45, description = 'Papá de la familia', 
                                           hobbies = 'Computación, gastronomía'
                                           )
   
   context = {
      'new_member': new_member
   }
   
   return render(request, '02_members.html', context = context)
   