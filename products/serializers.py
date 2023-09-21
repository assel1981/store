from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'categories')