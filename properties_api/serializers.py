from rest_framework import serializers
from properties.models import Property
from properties.search import SearchResults

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        # fields = ('id', 'title', 'price')
        fields = ('id', 'service_id', 'service_name', 'title', 'price', 'location', 'description', 'area', 'floor', 'type_of_property', 'type_of_building', 'number_of_rooms', 'create_date', 'modify_date', 'scrape_job_id')
        model = Property


class SearchResultSerializer(serializers.Serializer):
    offer_url = serializers.CharField()
    offer_url_path = serializers.CharField()
    main_image_url = serializers.CharField()
    title = serializers.CharField()
    price = serializers.CharField()
    price_per_square_meter = serializers.CharField()
    number_of_rooms = serializers.CharField()
    area = serializers.CharField()
    service= serializers.CharField()

class SearchResultsSerializer(serializers.Serializer):
    objects = serializers.ListField(child=SearchResultSerializer())