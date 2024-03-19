from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing properties.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
