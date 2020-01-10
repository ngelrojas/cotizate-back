from django.utils.timezone import now
from rest_framework import serializers
from core.models import Campaing, CampaingComplement
from core.models import Currency
from core.models import CategoryCampaing, TagCampaing
from tag.serializers import TagCampaingSerializer


class CurrencyPublicSerializer(serializers.ModelSerializer):
    """serializer public currencies"""

    class Meta:
        model = Currency
        fields = ('id', 'name', 'symbol',)


class CampaingListSerializer(serializers.ModelSerializer):
    """serializer campaing just list"""
    # tags = TagCampaingSerializer(many=True, read_only=True)
    currency = CurrencyPublicSerializer()

    class Meta:
        model = Campaing
        fields = (
                'id',
                'title',
                'slug',
                'city',
                'budget',
                'qty_days',
                'facebook',
                'twitter',
                'linkedin',
                'instagram',
                'website',
<<<<<<< HEAD
                'video',
                'excerpt',
                'description',
                'created_at',
                'updated_at',
                'is_enabled',
                'tags',
                'currencies',
                'category',
=======
                'currency',
>>>>>>> 0bee55a94b55adafd6453d10a40faee548f2b851
        )


class CampaingSerializer(serializers.ModelSerializer):
    """serializer for campaing"""
    currency = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=Currency.objects.all()
    )

    category = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=CategoryCampaing.objects.all()
    )

    class Meta:
        model = Campaing
        fields = (
                'id',
                'title',
                'slug',
                'city',
                'budget',
                'qty_days',
                'facebook',
                'twitter',
                'linkedin',
                'instagram',
                'website',
                'currency',
                'category',
        )

        read_only_fields = ('id',)


class CampaingCompSerializar(serializers.ModelSerializer):
    """serializer for campaing complementary"""
    tags = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=TagCampaing.objects.all()
    )

    class Meta:
        model = CampaingComplement
        fields = (
                'id',
                'video',
                'excerpt',
                'description',
                'created_at',
                'updated_at',
                'is_enabled',
                'campaing',
                'tags',
                'category',
        )

        read_only_fields = ('id',)

class CampaingSerializerPublic(serializers.ModelSerializer):
    """campaing serializer public"""
    # tags = TagCampaingSerializer(many=True, read_only=True)
    currency = CurrencyPublicSerializer()

    class Meta:
        model = Campaing
        fields = (
                'title',
                'slug',
                'city',
                'budget',
                'qty_days',
                'facebook',
                'twitter',
                'linkedin',
                'instagram',
                'website',
<<<<<<< HEAD
                'video',
                'excerpt',
                'description',
                'tags',
                'currencies',
                'category',
=======
                'currency',
>>>>>>> 0bee55a94b55adafd6453d10a40faee548f2b851
        )

        read_only_fields = ('id',)
