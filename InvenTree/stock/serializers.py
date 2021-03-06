from rest_framework import serializers

from .models import StockItem, StockLocation
from .models import StockItemTracking

from part.serializers import PartBriefSerializer
from InvenTree.serializers import UserSerializer, UserSerializerBrief

class LocationBriefSerializer(serializers.ModelSerializer):

    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = StockLocation
        fields = [
            'pk',
            'name',
            'pathstring',
            'url',
        ]


class StockTrackingSerializer(serializers.ModelSerializer):

    url = serializers.CharField(source='get_absolute_url', read_only=True)

    user = UserSerializerBrief(many=False, read_only=True)

    class Meta:
        model = StockItemTracking
        fields = [
            'pk',
            'url',
            'item',
            'date',
            'title',
            'notes',
            'quantity',
            'user',
            'system',
        ]

        read_only_fields = [
            'date',
            'user',
            'system',
            'quantity',
        ]


class StockItemSerializer(serializers.ModelSerializer):
    """ Serializer for a StockItem
    """
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    part = PartBriefSerializer(many=False, read_only=True)
    location = LocationBriefSerializer(many=False, read_only=True)

    class Meta:
        model = StockItem
        fields = [
            'pk',
            'uuid',
            'url',
            'part',
            'supplier_part',
            'location',
            'in_stock',
            #'belongs_to',
            #'customer',
            'quantity',
            'serial',
            'batch',
            'status',
            'notes',
            #'updated',
            #'stocktake_date',
            #'stocktake_user',
            #'review_needed',
        ]

        """ These fields are read-only in this context.
        They can be updated by accessing the appropriate API endpoints
        """
        read_only_fields = [
            'stocktake_date',
            'stocktake_user',
            'updated',
            #'quantity',
        ]


class StockQuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = StockItem
        fields = ('quantity',)


class LocationSerializer(serializers.ModelSerializer):
    """ Detailed information about a stock location
    """

    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = StockLocation
        fields = [
                  'pk',
                  'url',
                  'name',
                  'description',
                  'parent',
                  'pathstring'
                ]
