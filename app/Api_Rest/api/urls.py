from django.urls import path 
from .views import ArticuloView,PedidoView

urlpatterns = [
    path('articulos/',ArticuloView.as_view(),name='articulos_list'),
    path('pedidos/',PedidoView.as_view(),name='pedidos_list'),
     path('pedidos/<int:id>',PedidoView.as_view(),name='pedidos_process')
]