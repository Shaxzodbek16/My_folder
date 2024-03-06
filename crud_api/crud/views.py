from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CRUD
from .serializers import CRUDSerializer
from rest_framework import permissions
class CRUDViewSet(ModelViewSet):
    queryset = CRUD.objects.all()
    serializer_class = CRUDSerializer
    permission_classes = (permissions.AllowAny,)