from rest_framework import serializers
from .models import Countrie

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countrie
        fields =('id', 'nombre', 'capital')