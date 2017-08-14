
from django.conf.urls import url

from .views import ListarClientes, CrearCliente, ModificarCliente, EliminarCliente, \
PerfilCliente

from django.contrib.auth.decorators import login_required

urlpatterns = [
    #Clientes
    url(r'^listarclientes$', login_required(ListarClientes.as_view()), name='listar_clientes'),
    url(r'^crearclientes$', login_required(CrearCliente.as_view()), name='crear_clientes'),
    url(r'^modificarcliente/(?P<pk>\d+)$', login_required(ModificarCliente.as_view()), name='modificar_cliente'),
    url(r'^eliminarcliente/(?P<pk>\d+)$', login_required(EliminarCliente.as_view()), name='eliminar_cliente'),

    # Perfil del cliente
    url(r'^perfil/(?P<pk>\d+)$', login_required(PerfilCliente.as_view()), name='perfil_cliente'),
]