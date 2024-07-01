from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, ContactPersonViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r"suppliers", SupplierViewSet, basename="supplier")
router.register(r"contacts", ContactPersonViewSet, basename="contact")

urlpatterns = [
    path("", include(router.urls)),
]
