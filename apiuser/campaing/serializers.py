from rest_framework import serializers
from core.models import Campaing, Currency, TagCampaing
from tag.serializers import TagCampaingSerializer
from category.serializers import CategoryPublicGeneral


class CurrencyPublicSerializer(serializers.ModelSerializer):
    """serializer public currencies"""

    class Meta:
        model = Currency
        fields = ('id', 'name', 'symbol',)


class CampaingListSerializer(serializers.ModelSerializer):
    """serializer campaing just list"""
    tags = TagCampaingSerializer(many=True, read_only=True)
    currencies = CurrencyPublicSerializer()
    category = CategoryPublicGeneral()

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
                'video',
                'excerpt',
                'description',
                'created_at',
                'updated_at',
                'is_enabled',
                'tags',
                'currencies',
                'category',
        )


class CampaingSerializer(serializers.ModelSerializer):
    """serializer for campaing"""
    tags = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=TagCampaing.objects.all()
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
                'video',
                'excerpt',
                'description',
                'created_at',
                'updated_at',
                'is_enabled',
                'tags',
                'currencies',
                'category',
        )

        read_only_fields = ('id',)


class CampaingSerializerPublic(serializers.ModelSerializer):
    """campaing serializer public"""
    tags = TagCampaingSerializer(many=True, read_only=True)
    currencies = CurrencyPublicSerializer()

    class Meta:
        model = Campaing
        fields = (
                'title',
                'slug',
                'city',
                'budget',
                'qty_days',
                'video',
                'excerpt',
                'tags',
                'currencies',
                'category',
        )

        read_only_fields = ('id',)
