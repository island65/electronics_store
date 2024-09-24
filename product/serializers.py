from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product object serializer."""

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["arrears"]


class ProductListSerializer(serializers.ModelSerializer):
    """Product list object serializer."""

    class Meta:
        model = Product
        fields = ("id", "name", "product_model", "create_date", "company")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Product detail object serializer."""

    class Meta:
        model = Product
        fields = "__all__"


class ProductUpdateSerializer(serializers.ModelSerializer):
    """Product update object serializer."""

    class Meta:
        model = Product
        fields = "__all__"
