from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    # edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )

    class Meta:
        model = Product
        fields = ['pk',
                  'title',
                  'content',
                  'price',
                  'sale_price',
                  'my_discount',
                  'url',
                  #   'edit_url',
                  ]

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

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        elif not isinstance(obj, Product):
            return None
        return obj.get_discount()
