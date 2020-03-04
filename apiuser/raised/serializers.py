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

    def addraised(self, instance, validated_data):
        amount = 0
        count = 0
        current_amount = validated_data.get('amount', None)
        current_count = validated_data.get('count', None)
        amount = current_amount + instance.amount
        count = current_count + instance.count
        res = {
            'amount': amount,
            'count': count
        }
        return res

    def update(self, instance, validated_data):
        addr = self.addraised(instance, validated_data)
        instance.amount = addr['amount']
        instance.count = addr['count']
        instance.before_amount = instance.before_amount
        instance.save()
        return instance
