from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Producto, Pedido
from .serializers import ProductoSerializer, PedidoSerializer

@api_view(['GET'])
def productos_api(request):
    data = list(Producto.objects.values())
    return Response(data)

@api_view(['GET'])
def lista_productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle_producto(request, id):
    producto = Producto.objects.get(id=id)
    serializer = ProductoSerializer(producto)
    return Response(serializer.data)

@api_view(['POST'])
def crear_producto(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def actualizar_producto(request, id):
    producto = Producto.objects.get(id=id)
    serializer = ProductoSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return Response({"mensaje": "Eliminado"})

@api_view(['GET'])
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    serializer = PedidoSerializer(pedidos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_pedido(request):
    serializer = PedidoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def pagar(request):
    return Response({
        "estado": "aprobado",
        "mensaje": "Pago realizado con éxito"
        })

@api_view(['GET'])
def tracking(request, id):
    return Response({
        "pedido": id,
        "estado": "en camino",
        "ubicacion": "Santiago"
        })