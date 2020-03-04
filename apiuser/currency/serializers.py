from rest_framework import serializers
from core.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    """serializer for currencies """

    class Meta:
        model = Currency
        fields = (
                'id',
                'name',
                'symbol',)
        read_only_fields = ('id',)
