from rest_framework import serializers
from .models import Company, Car

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'  


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__' 
