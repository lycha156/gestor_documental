from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from .models import TipoDependencia, Dependencia
from .forms import DependenciaForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from historial.models import Historial

@login_required
def index(request):
    if request.method == 'POST':
        query = request.POST['query']
        dependencias = Dependencia.objects.filter( Q(nombre__icontains = query) | Q(telefono__icontains = query) | Q(tipo__tipo__icontains = query))[:50]
    else:
        dependencias = Dependencia.objects.all()[:50]

    context = {
        'dependencias': dependencias
    }
    return render(request, 'dependencias_index.html', context)


@login_required
def craete(request):
    form = DependenciaForm()
    if request.method == 'POST':
        form = DependenciaForm(request.POST)

        try:
            if form.is_valid():
                instancia = form.save()

                # HISTORIAL
                Historial.objects.create(accion="A", tabla="DEPENDENCIA", descripcion=f"{instancia}", usuario=request.user.username)
                # HISTORIAL

                messages.success(request, "Datos guardados en forma correcta.")
                return redirect('dependencias_index')
            else:
                messages.warning(request, 'Error al realizar la carga de los datos')
                return render(request, 'dependencias_create.html', context = {'form': form, 'validated': True})

        except Exception as e:
            messages.warning(request, f'Error al realizar la carga de datos. {e}')
            return redirect('dependencias_index')

    context = {'form': form}
    return render(request, 'dependencias_create.html', context)


@login_required
def update(request, id=id):
    obj = get_object_or_404(Dependencia, pk=id)
    form = DependenciaForm(request.POST or None, instance=obj)

    if request.method == 'POST':

        if form.is_valid():
            try:
                dependencia_original = Dependencia.objects.get(pk=id)
                form.save()

                # HISTORIAL
                Historial.objects.create(accion="M", tabla="DEPENDENCIA", descripcion=f'{dependencia_original} ==> {request.POST}', usuario=request.user.username)
                # HISTORIAL

                messages.success(request, "Datos actulizados en forma correcta.")
                return redirect('dependencias_index')
            except Exception as e:
                messages.warning(request, f'Error al actualizar los datos. {e}')
                return redirect('dependencias_index')
        else:
            messages.warning(request, 'Error al realizar la carga de los datos')
            return render(request, 'dependencias_create.html', context = {'form': form, 'validated': True})
    
    context = {
        'form': form
    }
    return render(request, 'dependencias_create.html', context)


@login_required
def show(request, id=id):
    dependencia = get_object_or_404(Dependencia, pk=id)

    context = {
        'dependencia': dependencia
    }
    return render(request, 'dependencias_show.html', context)


@login_required
def delete(request, id=id):
    dependencia = get_object_or_404(Dependencia, pk=id)
    if request.method == 'POST':
        try:
            exdependencia = Dependencia.objects.get(pk=id)
            dependencia.delete()

            # HISTORIAL
            Historial.objects.create(accion="B", tabla="DEPENDENCIA", descripcion=f'{exdependencia}', usuario=request.user.username)
            # HISTORIAL

            messages.warning(request, "La dependencia fue eliminada con exito.")
            return redirect('dependencias_index')
        except Exception as e:
            messages.warning(request, f"No es posible eliminar la dependencia. Error: {e}")
            return redirect("dependencias_index")
    
    context = {
        'dependencia': dependencia
    }
    return render(request, 'dependencias_delete.html', context)

