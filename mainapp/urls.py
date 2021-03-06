from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required

from mainapp.models import Producto

from .views import (
    Inscripcion,
    Empleado,
    Alumnos,
    Escuela,
    Home,
    AddCuota,
    Pagos,
    ShowTicket,
    CuotaActions,
    Dashboard,
    AddProducto,
    ProductoActions,
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
        "pagos/",
        Pagos.as_view(),
        name="pagos",
    ),
    path(
        "ticket/<int:ticket>/",
        ShowTicket.as_view(),
        name="ticket",
    ),
    path(
        "rmcuota/<int:cuota>/",
        CuotaActions.as_view(),
        name="rmcuota",
    ),
    path(
        "dashboard/",
        Dashboard.as_view(),
        name="rmcuota",
    ),
    path(
        "producto/",
        AddProducto.as_view(),
        name="producto",
    ),

    path(
        "",
        Home.as_view(),
        name="home",
    ),    
    path(
        "rmproducto/<int:id>/",
        ProductoActions.as_view(),
        name="rmproduct",
    ),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
