from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', context={
        'name': 'Matheus Augusto',
    })


def sobre(request):
    return HttpResponse('SOBRE')


def contato(request):
    return render(request, 'me-apague/temp.html')

