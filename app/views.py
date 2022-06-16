from django.http import Http404
from django.shortcuts import redirect, render
from .forms import ContactoForms, CustomUserCreationForm, ProductoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Contacto
from .models import Producto
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def home(request):
    return render(request, 'app/home.html')

def api(request):
    return render(request, 'app/api.html')

def recomendaciones(request):
    return render(request, 'app/recomendaciones.html')

def tiendas(request):
    productos = Producto.objects.all()
    data ={
        'productos' : productos
    }
    return render(request, 'app/tiendas.html', data)

def tips(request):
    return render(request, 'app/tips.html')

def tip1(request):
    return render(request, 'app/paginas_tips/tip1.html')
def tip2(request):
    return render(request, 'app/paginas_tips/tip2.html')
def tip3(request):
    return render(request, 'app/paginas_tips/tip3.html')
def tip4(request):
    return render(request, 'app/paginas_tips/tip4.html')
def tip5(request):
    return render(request, 'app/paginas_tips/tip5.html')



def contacto(request):
    data = {
        'form': ContactoForms()
    }
    if request.method == 'POST':
        formulario = ContactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Enviado correctamente")
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamnete")
            return redirect(to="home")
        else:
            data["form"] = formulario
    
    return render(request, 'registration/registro.html', data)

@permission_required('app.view_contacto')
def listar_contacto(request):
    queryset = request.GET.get('buscar')
    contacto = Contacto.objects.all()
    page = request.GET.get('page', 1)
    if queryset:
        contacto = Contacto.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(apellido__icontains = queryset)

    ).distinct()
    try:
        paginator = Paginator(contacto, 4)
        contacto = paginator.page(page)    
    except:
        raise Http404
    data ={
        'entity': contacto,
        'paginator': paginator,
    }
    return render(request, 'app/contacto/listar_contacto.html',data)


@permission_required('app.add_producto')
def agregar_producto(request):

    data = {
        'form': ProductoForm
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado correctamente")
        else:
            data["form"] = formulario

    return render(request, 'app/tienda/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'app/tienda/listar.html', data)
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'app/tienda/listar.html', data)

@permission_required('app.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id = id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to='listar_productos')
        data["form"] = formulario
            
        

    return render(request, 'app/tienda/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_productos")
