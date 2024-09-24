from rest_framework import serializers

from company.models import Company, Supplier


class CompanySerializer(serializers.ModelSerializer):
    """Company object serializer."""

    class Meta:
        model = Company
        fields = "__all__"


class CompanyListSerializer(serializers.ModelSerializer):
    """Company list object serializer."""

    class Meta:
        model = Company
        fields = ("id", "name", "email", "country", "city", "street", "number_bld", "owner")


class CompanyDetailSerializer(serializers.ModelSerializer):
    """Company detail object serializer."""

    class Meta:
        model = Company
        fields = "__all__"


class CompanyUpdateSerializer(serializers.ModelSerializer):
    """Company update object serializer."""

    class Meta:
        model = Company
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    """Supplier object serializer."""

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierUpdateSerializer(serializers.ModelSerializer):
    """Supplier update object serializer."""
    class Meta:
        model = Supplier
        fields = ('customer', 'supplier', 'debt')


class SupplierListSerializer(serializers.ModelSerializer):
    """Supplier list object serializer."""
    class Meta:
        model = Supplier
        fields = ('supplier_name', 'owner', 'id')
