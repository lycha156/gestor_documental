from django.shortcuts import render, redirect, get_object_or_404
from .models import Grupo, Documento, DocumentoRelacion
from django.contrib import messages
from django.db.models import Q
from .forms import GrupoForm, DocumentoForm
from django.contrib.auth.decorators import login_required

# DOCUMENTACION
def index(request):
    if request.method == 'POST':
        query = request.POST['query']
        documentos = Documento.objects.filter( Q(estado__estado__icontains = query) | Q(fecha__icontains = query) | Q(codigo__icontains = query) | Q(grupo__grupo__icontains = query) | Q(iniciador__nombre__icontains = query) | Q(destino__nombre__icontains = query) | Q(tags__icontains = query) )[:50]
    else:
        documentos = Documento.objects.all()[:50]

    context = {
        'documentos': documentos
    }
    return render(request, 'documentacion_index.html', context)


@login_required
def create(request, id=None):
    form = DocumentoForm()
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)

        try:
            if form.is_valid():
                instancia = form.save(commit=False)
                instancia.usuario = request.user
                form.save()

                # RELACION DOCUMENTO
                if request.POST['padre'] is not None:
                    padre = Documento.objects.get(id=request.POST['padre'])
                    documento = Documento.objects.get(id=instancia.id)
                    relacion = DocumentoRelacion(documento=documento, padre=padre)
                    relacion.save()

                messages.success(request, "Datos guardados en forma correcta.")
                return redirect('documentacion_index')
            else:
                messages.warning(request, 'Error al realizar la carga de los datos')
                return render(request, 'documentacion_create.html', context = {'form': form, 'validated': True, 'padre': id})

        except Exception as e:
            messages.warning(request, f'Error al realizar la carga de datos. {e}')
            return redirect('documentacion_index')

    context = {
        'form': form,
        'padre': id
    }
    
    return render(request, 'documentacion_create.html', context)


@login_required
def update(request, id=id):
    obj = get_object_or_404(Documento, pk=id)
    form = DocumentoForm(request.POST or None, request.FILES or None, instance=obj)

    if request.method == 'POST':

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Datos actulizados en forma correcta.")
                return redirect('documentacion_index')
            except Exception as e:
                messages.warning(request, f'Error al actualizar los datos. {e}')
                return redirect('documentacion_index')
        else:
            messages.warning(request, 'Error al realizar la carga de los datos')
            return render(request, 'documentacion_create.html', context = {'form': form, 'validated': True})
    
    context = {
        'form': form
    }
    return render(request, 'documentacion_create.html', context)


def show(request, id=id):
    documento = get_object_or_404(Documento, pk=id)
    relacionados = DocumentoRelacion.objects.filter(padre = documento)
    padres = DocumentoRelacion.objects.filter(documento = documento)

    context = {
        'documento': documento,
        'relacionados': relacionados,
        'padres': padres
    }
    return render(request, 'documentacion_show.html', context)


def delete(request, id=id):
    documento = get_object_or_404(Documento, pk=id)
    if request.method == 'POST':
        try:
            documento.delete()
            messages.warning(request, "El Documento fue eliminado con exito.")
            return redirect('documentacion_index')
        except Exception as e:
            messages.warning(request, f"No es posible eliminar el documento. Error: {e}")
            return redirect("documentacion_index")
    
    context = {
        'documento': documento
    }
    return render(request, 'documentacion_delete.html', context)


# GRUPOS
def grupo_index(request):
    if request.method == 'POST':
        query = request.POST['query']
        grupos = Grupo.objects.filter( Q(grupo__icontains = query))[:50]
    else:
        grupos = Grupo.objects.all()[:50]

    context = {
        'grupos': grupos
    }
    return render(request, 'grupos_index.html', context)

def grupo_create(request):
    form = GrupoForm()
    if request.method == 'POST':
        form = GrupoForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Datos guardados en forma correcta.")
                return redirect('grupos_index')
            else:
                messages.warning(request, 'Error al realizar la carga de los datos')
                return render(request, 'grupos_create.html', context = {'form': form, 'validated': True})

        except Exception as e:
            messages.warning(request, f'Error al realizar la carga de datos. {e}')
            return redirect('grupos_index')

    context = {'form': form}
    return render(request, 'grupos_create.html', context)


def grupo_update(request, id=id):
    obj = get_object_or_404(Grupo, pk=id)
    form = GrupoForm(request.POST or None, instance=obj)

    if request.method == 'POST':

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Datos actulizados en forma correcta.")
                return redirect('grupos_index')
            except Exception as e:
                messages.warning(request, f'Error al actualizar los datos. {e}')
                return redirect('grupos_index')
        else:
            messages.warning(request, 'Error al realizar la carga de los datos')
            return render(request, 'grupos_create.html', context = {'form': form, 'validated': True})
    
    context = {
        'form': form
    }
    return render(request, 'grupos_create.html', context)

def grupo_show(request, id=id):
    pass

def grupo_delete(request, id=id):
    grupo = get_object_or_404(Grupo, pk=id)
    if request.method == 'POST':
        try:
            grupo.delete()
            messages.warning(request, "Grupo fue eliminado con exito.")
            return redirect('grupos_index')
        except Exception as e:
            messages.warning(request, f"No es posible eliminar el grupo. Error: {e}")
            return redirect("grupos_index")
    
    context = {
        'grupo': grupo
    }
    return render(request, 'grupos_delete.html', context)