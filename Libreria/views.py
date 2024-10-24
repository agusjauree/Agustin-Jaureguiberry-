from django.http import Http404
from django.shortcuts import redirect, render

from Libreria.models import Libro

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()  # Obtener todos los libros
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        fecha_publicacion = request.POST['fecha_publicacion']
        Libro.objects.create(titulo=titulo, autor=autor, fecha_publicacion=fecha_publicacion)
        return redirect('libros')
    return render(request, 'libros/crear.html')

def editar(request, id):
    try:
        libro = Libro.objects.get(id=id)
    except Libro.DoesNotExist:
        raise Http404("El libro no existe")
    
    if request.method == 'POST':
        libro.titulo = request.POST['titulo']
        libro.autor = request.POST['autor']
        libro.fecha_publicacion = request.POST['fecha_publicacion']
        libro.save()
        return redirect('libros')
    
    return render(request, 'libros/editar.html', {'libro': libro})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')