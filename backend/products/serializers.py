from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from . import validators
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )
    title = serializers.CharField(
        validators=[
            validators.validate_title_no_hello,
            validators.unique_product_title
        ])

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'content',
            'owner',
            'price',
            'sale_price',
            'url',
            'edit_url',
            'public',
        ]

    def get_my_user_data(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
        }

    def get_url(self, obj):
        # return f'api/v2/products/{obj.pk}'
        request = self.context.get('request')  # self.request

        if request is None:
            return None

        return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)

    def get_edit_url(self, obj):
        # return f'api/v2/products/{obj.pk}'
        request = self.context.get('request')  # self.request

        if request is None:
            return None

        return reverse('product-edit', kwargs={'pk': obj.pk}, request=request)
