from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductSerializer


class ProductListAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer