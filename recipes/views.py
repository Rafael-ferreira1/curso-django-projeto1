from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'recipes/home.html', context={
        'name': 'Rafael',
    })# busca pagina dentro de templates nao e necessario falar a pasta

