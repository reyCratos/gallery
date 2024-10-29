from django.shortcuts import render


def lista_genero(request, nombre):
    lista_g = ['terror','comedia','drama','romance']
    contexto = {'nombre':nombre, 'lista_g':lista_g}
    return render(request, 'pagina1.html',contexto)