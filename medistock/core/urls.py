from django.contrib import admin
from django.urls import path
from . import views
from .api_views import productos_api

urlpatterns = [
    path('', views.login_view, name="login"),
    path('cliente/', views.cliente_view, name="cliente"),
    path('ejecutivo/', views.ejecutivo_view, name="ejecutivo"),
    path('logistica/', views.logistica_view, name="logistica"),
    path('finanzas/', views.finanzas_view, name="finanzas"),
]

urlpatterns += [
    path('api/productos/', productos_api),
]
