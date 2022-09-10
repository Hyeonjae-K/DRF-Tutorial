from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(
        StaffEditorPermissionMixin,
        generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     # authentication.TokenAuthentication,
    #     TokenAuthentication,
    # ]
    # permission_classes = [
    #     permissions.IsAdminUser,
    #     IsStaffEditorPermission,
    # ]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        # email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        instance = serializer.save(content=content)
        # send a Django signal


class ProductDetailAPIView(
        StaffEditorPermissionMixin,
        generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(
        StaffEditorPermissionMixin,
        generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title


class ProductDeleteAPIView(
        StaffEditorPermissionMixin,
        generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


class ProductMixinView(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        generics.GenericAPIView,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        # print(args, kwargs)
        pk = kwargs.get('pk')

        if pk is not None:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # create an item
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = 'this is a single view doing cool stuff'

        serializer.save(content=content)
        return Response(serializer.data)


# class ProductListAPIView(generics.ListAPIView):
#     """
#     Not gonna use this method
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# adds confusion but flexible.
# this is why using generic views
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        else:
            # list view
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)

    if method == 'POST':
        # create an item
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None

            if content is None:
                content = title

            serializer.save(content=content)
            return Response(serializer.data)
        return Response({'invalid': 'not good data'}, status=400)

    # product_detail_view = ProductDetailAPIView.as_view()
    # product_create_view = ProductCreateAPIView.as_view()
