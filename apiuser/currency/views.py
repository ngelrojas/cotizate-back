from rest_framework import viewsets
from core.models import Currency
from currency import serializers


class CurrencyPublic(viewsets.ModelViewSet):
    """
    list:
        show all currencies
    """
    queryset = Currency.objects.all()
    serializer_class = serializers.CurrencySerializer
