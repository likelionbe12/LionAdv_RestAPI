from django.http import JsonResponse, HttpResponse
from .models import Product
from .serializers import serialize_product
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return JsonResponse({'products': [serialize_product(p) for p in products]}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(**data)
        return JsonResponse(serialize_product(product), status=201)

@csrf_exempt
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        return JsonResponse(serialize_product(product))
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(product, field, value)
        product.save()
        return JsonResponse(serialize_product(product))
    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)
