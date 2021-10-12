from rest_framework import serializers
from .models import Fintastic

class FintasticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fintastic
        fields = ('id', 'title', 'description')