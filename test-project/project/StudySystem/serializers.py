from .models import Lesson, Product, AccesToProduct
from rest_framework import  serializers 

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson 
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'

class AccesToProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccesToProduct
        fields = '__all__'

        