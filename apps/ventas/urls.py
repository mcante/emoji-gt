
from django.conf.urls import url

from .views import ListarPedido, CrearPedido, ModificarPedido, EliminarPedido, \
ListarDtPedido, CrearDetallePedido, ModificarDetallePedido, EliminarDetallePedido, \
MapaPedido

from django.contrib.auth.decorators import login_required

urlpatterns = [
    #PEDIDOS
    url(r'^listarpedidos$', login_required(ListarPedido.as_view()), name='listar_pedidos'),
    url(r'^crearpedido$', login_required(CrearPedido.as_view()), name='crear_pedido'),
    url(r'^modificarpedido/(?P<pk>\d+)$', login_required(ModificarPedido.as_view()), name='modificar_pedido'),
    url(r'^eliminarpedido/(?P<pk>\d+)$', login_required(EliminarPedido.as_view()), name='eliminar_pedido'),

    #DETALLES
    url(r'^listarpedidodt/(?P<pk>\d+)$', login_required(ListarDtPedido.as_view()), name='listar_pedidos_con_detalle'),
    url(r'^nuevodetallepedido$', login_required(CrearDetallePedido.as_view()), name='crear_detalle_pedido'),
    url(r'^modificardetallepedido/(?P<pk>\d+)$', login_required(ModificarDetallePedido.as_view()), name='modificar_detalle_pedido'),
    url(r'^eliminardetallepedido/(?P<pk>\d+)$', login_required(EliminarDetallePedido.as_view()), name='eliminar_detalle_pedido'),

    # MAPA
    url(r'^mapa$', login_required(MapaPedido.as_view()), name='mapa_pedido'),
]
