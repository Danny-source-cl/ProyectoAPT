from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate,login
from .forms import ProductoForm

def menu(request):
    listaproductos= Producto.objects.all()
    return render(request,"menu.html", {"productos": listaproductos})

def registrar(request): 
    data = {
         'form': ProductoForm()}         
    if request.method == 'POST':
        formulario = ProductoForm(data= request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Producto guardado"                                                
    return render(request, 'lista_productos.html', data)

def modificar(request, id):
    
    productos = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=Producto) }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=Producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="mostrar")
        data["form"]=formulario
            
    return render(request,'menu.html',data)  

def lista_productos(request):
    productos = Producto.objects.all()
    data = {
        "productos" : productos
    }
    return render (request,'menu.html', data)
    
def eliminar (request,id):
    productos= get_object_or_404(Producto, id=id)
    productos.delete()
    return redirect(to="mostrar")   