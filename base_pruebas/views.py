from django.shortcuts import render


def base_prueba(request):
    template = 'base_pruebas/pruebas_js.html'

    context = {
        'Valor_prueba': '100'
    }
    return render(request, template, context)
