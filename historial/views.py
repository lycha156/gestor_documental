from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Historial

@login_required()
def administracion(request):
    # solo staff
    if request.user.is_staff == False:
        return redirect('documentacion_index')

    historiales = Historial.objects.all()

    context = {
        'historiales': historiales
    }
    return render(request, 'historial_administracion.html', context)


@login_required
def show(request, id=id):
    # solo staff
    if request.user.is_staff == False:
        return redirect('documentacion_index')

    historial = get_object_or_404(Historial, pk=id)

    context = {
        'historial': historial
    }
    return render(request, 'historial_show.html', context)
