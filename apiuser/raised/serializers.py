from rest_framework import serializers
from core.models import Raised


class RaisedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Raised
        fields = (
                'id',
                'amount',
                'before_amount',
                'count',
        )

    def update(self, instance, validated_data):
        instance.amount = validated_data.get(
                'amount',
                instance.amount
        )
        instance.before_amount = validated_data.get(
                'before_amount',
                instance.before_amount
        )
        instance.count = validated_data.get(
                'count',
                instance.count
        )
        instance.save()
        return instance
