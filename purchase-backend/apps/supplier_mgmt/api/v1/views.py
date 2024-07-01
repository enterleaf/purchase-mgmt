from rest_framework import viewsets
from apps.supplier_mgmt.models import Supplier, ContactPerson
from .serializers import SupplierSerializer, ContactPersonSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    """
    Viewset for creating, viewing and editing Supplier instances.
    """

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ContactPersonViewSet(viewsets.ModelViewSet):
    """
    Viewset for creating, viewing and editing contactperson instances.
    """

    queryset = ContactPerson.objects.all()
    serializer_class = ContactPersonSerializer
