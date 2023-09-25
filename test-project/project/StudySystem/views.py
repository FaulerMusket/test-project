from .models import Lesson, Product, AccesToProduct
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LessonSerializer, ProductSerializer, AccesToProductSerializer

class LessonViewSet(viewsets.ModelViewSet):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permissions_classes = [
        permissions.IsAuthenticated
    ]

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions_classes = [
        permissions.IsAuthenticated
    ]

class AccesToProductViewSet(viewsets.ModelViewSet):

    queryset = AccesToProduct.objects.all()
    serializer_class = AccesToProductSerializer
    permissions_classes = [
        permissions.IsAuthenticated
    ]


