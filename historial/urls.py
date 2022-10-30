from  django.urls import path
from . import views

urlpatterns = [
    path('administracion', views.administracion, name="historial_administracion"),
    path('show/<int:id>', views.show, name="historial_show"),
]
