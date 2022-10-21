from django.shortcuts import render

def index(request):
    return render(request, 'documentacion_index.html')
