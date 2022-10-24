from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dependencias_index"),
    path('create', views.craete, name="dependencias_create"),
    path('update/<int:id>', views.update, name="dependencias_update"),
    path('show/<int:id>', views.show, name="dependencias_show"),
    path('delete/<int:id>', views.delete, name="dependencias_delete"),
]