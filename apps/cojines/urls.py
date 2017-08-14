
from django.conf.urls import url

from .views import ListarMateriales, CrearMateriales, ModificarMaterial, EliminarMaterial, \
ListarCojines, CrearCojines, ModificarCojines, EliminarCojines

from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Materiales
    url(r'^listarmateriales$', login_required(ListarMateriales.as_view()), name='listar_materiales'),
    url(r'^crearmaterial$', login_required(CrearMateriales.as_view()), name='crear_materiales'),
    url(r'^modificarmaterial/(?P<pk>\d+)$', login_required(ModificarMaterial.as_view()), name='modificar_material'),
    url(r'^eliminarmaterial/(?P<pk>\d+)$', login_required(EliminarMaterial.as_view()), name='eliminar_material'),

    # Cojines
    url(r'^listarcojines$', login_required(ListarCojines.as_view()), name='listar_cojines'),
    url(r'^crearcojin$', login_required(CrearCojines.as_view()), name='crear_cojin'),
    url(r'^modificarcojin/(?P<pk>\d+)$', login_required(ModificarCojines.as_view()), name='modificar_cojin'),
    url(r'^eliminarcojin/(?P<pk>\d+)$', login_required(EliminarCojines.as_view()), name='eliminar_cojin'),

]
