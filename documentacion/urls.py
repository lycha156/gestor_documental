from django.urls import path
from . import views

urlpatterns = [
    # docuementacion
    path('', views.index, name="documentacion_index"),
    path('create/', views.create, name="documentacion_create"),
    path('create/<int:id>', views.create, name="documentacion_create_relacion"),
    path('update/<int:id>', views.update, name="documentacion_update"),
    path('show/<int:id>', views.show, name="documentacion_show"),
    path('delete/<int:id>', views.delete, name="documentacion_delete"),

    # documentos relacionados
    path("relacion/delete/<int:id>", views.relacion_delete, name="relaciones_delete"),
    
    # grupos
    path('grupos/', views.grupo_index, name="grupos_index"),
    path('grupos/create', views.grupo_create, name="grupos_create"),
    path('grupos/update/<int:id>', views.grupo_update, name="grupos_update"),
    path('grupos/show/<int:id>', views.grupo_show, name="grupos_show"),
    path('grupos/delete/<int:id>', views.grupo_delete, name="grupos_delete"),
]