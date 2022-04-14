from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Articulo, Pedido
import json
# Create your views here.


class ArticuloView(View):

    def get(self, request):
        articulos = list(Articulo.objects.values())

        if len(articulos) > 0:
            datos = {'message': "Success", 'articulos': articulos}
        else:
            datos = {'message': "Articulos no encontrados"}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def delete(self, request):
        pass


class PedidoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            pedidos=list(Pedido.objects.filter(id=id).values())
            if len(pedidos)>0:
                pedido=pedidos[0]
                datos = {'message': "Success", 'pedido': pedido}
        else:
             pedidos = list(Pedido.objects.values())

        if len(pedidos) > 0:
            datos = {'message': "Success", 'pedidos': pedidos}
        else:
            datos = {'message': "Pedido no encontrados"}
        return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Pedido.objects.create(
        nPedido=jd['nPedido'], fechaCreacion=jd['fechaCreacion'], precioSnImp=jd['precioSnImp'], porcentajeImp=jd['porcentajeImp'], precioCnImuesto=jd['precioCnImuesto'], moneda=jd['moneda'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def delete(self, request,id):

        pedidos= list(Pedido.objects.filter(id=id).values())
        if len(pedidos) > 0: 
            Pedido.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Pedido no encontrado"}
        return JsonResponse(datos)

