from django.shortcuts import render, redirect, get_object_or_404
from .models import Grupo, Documento, DocumentoRelacion
from django.contrib import messages
from django.db.models import Q
from .forms import GrupoForm, DocumentoForm
from django.contrib.auth.decorators import login_required
from historial.models import Historial

# DOCUMENTACION
@login_required
def index(request):
    if request.method == 'POST':
        query = request.POST['query']
        documentos = Documento.objects.filter( Q(estado__estado__icontains = query) | Q(fecha__icontains = query) | Q(codigo__icontains = query) | Q(grupo__grupo__icontains = query) | Q(iniciador__nombre__icontains = query) | Q(destino__nombre__icontains = query) | Q(tags__icontains = query) )[:10]
    else:
        documentos = Documento.objects.all()[:10]

    context = {
        'documentos': documentos
    }
    return render(request, 'documentacion_index.html', context)


@login_required
def create(request, id=False):
    # @id Id de documento de referencia para ser asignado como documento padre del nuevo documento.
    form = DocumentoForm()
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)

        try:
            if form.is_valid():
                instancia = form.save(commit=False)
                instancia.usuario = request.user
                form.save()

                # HISTORIAL
                Historial.objects.create(accion="A", tabla="DOCUMENTO", descripcion=f"{instancia.historial}", usuario=request.user.username)
                # HISTORIAL

                # RELACION DOCUMENTO
                # Solamente se guarda si se paso documento de referencia, sino, se ignora el codigo siguiente.
                if request.POST['padre'] != 'False':
                    padre = Documento.objects.get(id=request.POST['padre'])
                    documento = Documento.objects.get(id=instancia.id)
                    relacion = DocumentoRelacion(documento=documento, padre=padre)
                    relacion.save()

                    # HISTORIAL
                    Historial.objects.create(accion="A", tabla="DOCUMENTO-RELACION", descripcion=f"HIJO: {documento.descripcion_corta} => PADRE: {padre.descripcion_corta}", usuario=request.user.username)
                    # HISTORIAL

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
                documento_original = Documento.objects.get(pk=id)
                form.save()
                # HISTORIAL
                Historial.objects.create(accion="M", tabla="DOCUMENTO", descripcion=f'{documento_original.historial} ==> {request.POST}', usuario=request.user.username)
                # HISTORIAL
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


@login_required
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


@login_required
def delete(request, id=id):
    documento = get_object_or_404(Documento, pk=id)
    if request.method == 'POST':
        try:
            exdocumento = Documento.objects.get(pk=id)
            documento.delete()
            # HISTORIAL
            Historial.objects.create(accion="B", tabla="DOCUMENTO", descripcion=f'{exdocumento.historial}', usuario=request.user.username)
            # HISTORIAL
            messages.warning(request, "El Documento fue eliminado con exito.")
            return redirect('documentacion_index')
        except Exception as e:
            messages.warning(request, f"No es posible eliminar el documento. Error: {e}")
            return redirect("documentacion_index")
    
    context = {
        'documento': documento
    }
    return render(request, 'documentacion_delete.html', context)

# RELACIONES
@login_required
def relacion_delete(request, id=id):
    relacion = get_object_or_404(DocumentoRelacion, pk=id)
    if request.method == 'POST':
        try:
            exrelacion = DocumentoRelacion.objects.get(pk=id)
            relacion.delete()

            # HISTORIAL
            Historial.objects.create(accion="B", tabla="DOCUMENTO-RELACION", descripcion=f'{exrelacion}', usuario=request.user.username)
            # HISTORIAL

            messages.success(request, "Relacion entre documentos eliminada con exito.")
            return redirect('grupos_index')
        except Exception as e:
            messages.warning(request, f"No es posible eliminar la relacion entre los documentos. Error: {e}")
            return redirect("grupos_index")
    
    context = {
        'relacion': relacion
    }
    return render(request, 'relaciones_delete.html', context)


# GRUPOS
@login_required
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


@login_required
def grupo_create(request):
    form = GrupoForm()
    if request.method == 'POST':
        form = GrupoForm(request.POST)

        try:
            if form.is_valid():
                instancia = form.save()
                # HISTORIAL
                Historial.objects.create(accion="A", tabla="GRUPO", descripcion=f"{instancia}", usuario=request.user.username)
                # HISTORIAL
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


@login_required
def grupo_update(request, id=id):
    obj = get_object_or_404(Grupo, pk=id)
    form = GrupoForm(request.POST or None, instance=obj)

    if request.method == 'POST':

        if form.is_valid():
            try:
                grupo_original = Grupo.objects.get(pk=id)
                form.save()
                # HISTORIAL
                Historial.objects.create(accion="M", tabla="GRUPO", descripcion=f'{grupo_original} ==> {request.POST}', usuario=request.user.username)
                # HISTORIAL
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


@login_required
def grupo_show(request, id=id):
    pass


@login_required
def grupo_delete(request, id=id):
    grupo = get_object_or_404(Grupo, pk=id)
    if request.method == 'POST':
        try:
            exgrupo = Grupo.objects.get(pk=id)
            grupo.delete()

            # HISTORIAL
            Historial.objects.create(accion="B", tabla="GRUPO", descripcion=f'{exgrupo}', usuario=request.user.username)
            # HISTORIAL

            messages.warning(request, "Grupo fue eliminado con exito.")
            return redirect('grupos_index')
        except Exception as e:
            messages.warning(request, f"No es posible eliminar el grupo. Error: {e}")
            return redirect("grupos_index")
    
    context = {
        'grupo': grupo
    }
    return render(request, 'grupos_delete.html', context)