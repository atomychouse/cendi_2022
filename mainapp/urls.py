from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required

from .views import (
    Inscripcion,
    Empleado,
    Alumnos,
    Escuela,
    Home,
    AddCuota,
)
urlpatterns = [
    path(
        "inscripcion/",
        Inscripcion.as_view(),
        name="inscripcion",
    ),
    path(
        "escuela/",
        Escuela.as_view(),
        name="escuela",
    ),
    path(
        "cuota/",
        AddCuota.as_view(),
        name="add_cuota",
    ),

    path(
        "alumnos/",
        Alumnos.as_view(),
        name="alumnos",
    ),
    path(
        "",
        Home.as_view(),
        name="home",
    ),    


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
