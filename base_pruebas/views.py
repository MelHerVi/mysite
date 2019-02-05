from django.shortcuts import render

def base_prueba(request):
    return render(request, 'base_pruebas/base_prueba.html', {})
