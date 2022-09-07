from django.urls import path

from . import views

urlpatterns = [
    # path('<int:pk', views.product_detail_view),
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
]
