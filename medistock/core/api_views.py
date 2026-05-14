from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Producto, Pedido
from .serializers import ProductoSerializer, PedidoSerializer
from django.views.decorators.csrf import csrf_exempt


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
    pedido = Pedido.objects.create(
        total=0, 
        usuario=request.user
        )
    productos = request.data.get("productos", [])
    total = 0
    for p in productos:
        producto = Producto.objects.get(id=p["id"])
        pedido.productos.add(producto)
        total += producto.precio
    pedido.total = total
    pedido.save()
    return Response({
        "mensaje": "pedido creado"
    })

@api_view(['POST'])
def pagar(request):
    return Response({
        "mensaje": "pago realizado"
    })

@api_view(['GET'])
def tracking(request, id):
    return Response({
        "pedido": id,
        "estado": "en camino",
        "ubicacion": "Santiago"
        })