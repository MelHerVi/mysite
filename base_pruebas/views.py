from django.shortcuts import render

def base_prueba(request):
    context  = {
        'Pepe': '100',
        'adios': 'que tal'
    }
    return render(request, 'base_pruebas/base_prueba.html', context)
