from rest_framework.routers import DefaultRouter
from .views import CRUDViewSet
router = DefaultRouter()
router.register(r'crud', CRUDViewSet)