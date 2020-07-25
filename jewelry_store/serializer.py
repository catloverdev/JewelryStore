from rest_framework import serializers
from jewelry_store.models import Product, ProductPrice, Client, Status, Purchase


class ProductListSerializer(serializers.ModelSerializer):
    """Список изделий"""

    class Meta:
        model = Product
        fields = ("id_product", "title")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Изделие"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    material = serializers.SlugRelatedField(slug_field="name", read_only=True)
    gems = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Product
        fields = "__all__"


class PriceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPrice
        fields = '__all__'


class PriceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPrice
        exclude = ('id', )


class ClientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ClientDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        exclude = ('id', )


class PurchaseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = "__all__"


class StatusListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = "__all__"


class StatusDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = "__all__"


class StatusCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        exclude = ('id', )

    def create(self, validated_data):
        status = Status.objects.update_or_create(
            id=validated_data.get('ip', None),
            purchase=validated_data.get('purchase', None),
            date=validated_data.get('date', None),
            defaults={'status': validated_data.get('status')}
        )
        return status
