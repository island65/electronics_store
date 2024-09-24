from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from company.models import Company, Supplier
from company.paginators import CompanyPaginator, SuppliersPaginator
from company.permissions import IsCompanyOwner, IsSupplierOwner

from company.serializers import CompanySerializer, CompanyDetailSerializer, CompanyListSerializer, \
    CompanyUpdateSerializer, SupplierSerializer, SupplierListSerializer, SupplierUpdateSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """Company view set."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = CompanyPaginator
    filter_backends = (filters.SearchFilter,)
    search_fields = ("country",)

    def get_permissions(self):
        """Checking company access."""
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
            self.serializer_class = CompanySerializer
        if self.action in ["list"]:
            self.permission_classes = [AllowAny]
            self.serializer_class = CompanyListSerializer
        if self.action in ["retrieve"]:
            self.permission_classes = [IsAuthenticated, IsCompanyOwner]
            self.serializer_class = CompanyDetailSerializer
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsCompanyOwner]
            self.serializer_class = CompanyUpdateSerializer
        return super().get_permissions()

    def perform_create(self, serializer):
        """Create company object from serializer."""
        company = serializer.save()
        company.owner = self.request.user
        company.save()
        return company


class SupplierViewSet(viewsets.ModelViewSet):
    """Supplier view set."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = SuppliersPaginator

    def get_permissions(self):
        """Checking supplier access."""
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        if self.action == "list":
            self.permission_classes = [IsAuthenticated]
            self.serializer_class = SupplierListSerializer
        if self.action in ["retrieve"]:
            self.permission_classes = [IsAuthenticated, IsSupplierOwner]
            self.serializer_class = SupplierSerializer
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsSupplierOwner]
            self.serializer_class = SupplierUpdateSerializer
        return super().get_permissions()

    def perform_create(self, serializer):
        """Before saving the supplier, add the owner."""
        supplier = serializer.save()
        customer = Company.objects.get(id=supplier.customer)
        supplier.owner = self.request.user
        supplier.save()

        if customer.company_type == 'individual' or customer.company_type == 'retail':
            Company.objects.filter(id=customer.id).update(
                level=2, suppliers_name=supplier.supplier.name,
                supplier_id=supplier.supplier.id,
            )
            supplier.supplier_name = customer.name
            supplier.owner = self.request.user
            supplier.save()
        elif customer.company_type == 'factory':
            supplier.supplier_name = customer.name
            supplier.save()
            Company.objects.filter(id=customer.id).update(
                level=1, suppliers_name=supplier.supplier.name,
                supplier_id=supplier.supplier.id
            )
        return supplier

    def perform_update(self, serializer):
        """Before saving the supplier, add the owner."""
        supplier = serializer.save()
        customer = Company.objects.get(id=supplier.customer)

        if customer.company_type == 'individual' or customer.company_type == 'retail':
            supplier.supplier_name = customer.name
            supplier.owner = self.requests.user
            supplier.save()
            Company.objects.filter(id=customer.id).update(
                level=2, suppliers_name=supplier.supplier.name,
                supplier_id=supplier.supplier.id,
            )
        elif customer.company_type == 'factory':
            supplier.supplier_name = customer.name
            supplier.owner = self.request.user
            supplier.save()
            Company.objects.filter(id=customer.id).update(
                level=1, suppliers_name=supplier.supplier.name,
                supplier_id=supplier.supplier.id
            )
        return supplier
