from django.shortcuts import render



def index(request):
    titulo = 'index'
    
    context = {
        'titulo': titulo
    }
    
    return render(request, 'base.html', context) 
