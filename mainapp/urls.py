from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required

from .views import (
    Inscripcion,
    Empleado,
    Alumnos,
)
urlpatterns = [
    # path(
    #     "login",
    #     Login.as_view(),
    #     name="login",
    # ),
    path(
        "inscripcion/",
        Inscripcion.as_view(),
        name="inscripcion",
    ),
    path(
        "alumnos/",
        Alumnos.as_view(),
        name="alumnos",
    ),

    path(
        "",
        Empleado.as_view(),
        name="alumno",
    ),    

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
