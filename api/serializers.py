
from rest_framework import serializers
from .models import device

class deviceSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model =device
        fields = ('owner','make',
                  'light1isON','light2isON','light3isON',
                  'stove1State','fan1State','geyser1State','homeTemp')
        read_only_fields = ('date_registered','last_updated')