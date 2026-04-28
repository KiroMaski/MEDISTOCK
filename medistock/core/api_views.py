from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Producto

@api_view(['GET'])
def productos_api(request):
    data = list(Producto.objects.values())
    return Response(data)