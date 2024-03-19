from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'url', 'seo_title', 'seo_description', 'url_image', 
                  'data_price', 'data_room', 'data_area', 'data_bath', 
                  'data_type', 'in_visit', 'need_call', 'visit_date', 'notes']