from django.contrib import admin
from django.urls import path
from . import views, api_views
from .api_views import productos_api

urlpatterns = [
    #vistas web
    path('', views.login_view, name="login"),
    path('cliente/', views.cliente_view, name="cliente"),
    path('ejecutivo/', views.ejecutivo_view, name="ejecutivo"),
    path('logistica/', views.logistica_view, name="logistica"),
    path('finanzas/', views.finanzas_view, name="finanzas"),
    path('tracking/', views.tracking_view, name="Tracking"),
    
    #API
    path('api/productos/', api_views.lista_productos),
    path('api/productos/<int:id>/', api_views.detalle_producto),
    path('api/productos/crear/', api_views.crear_producto),
    path('api/productos/actualizar/<int:id>/', api_views.actualizar_producto),
    path('api/productos/eliminar/<int:id>/', api_views.eliminar_producto),
    path('api/pedidos/', api_views.lista_pedidos),
    path('api/pedidos/crear/', api_views.crear_pedido),
    path('api/pagar/', api_views.pagar),
    path('api/tracking/<int:id>/', api_views.tracking),
]

urlpatterns += [
    path('api/productos/', productos_api),
]