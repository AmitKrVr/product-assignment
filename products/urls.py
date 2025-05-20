from django.urls import path
from .views import (
    ProductListCreate,
    ProductDetail,
    add_product,
    product_list_view,
    product_detail_view
)

urlpatterns = [
    # API endpoints
    path('api/products/', ProductListCreate.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

    # Frontend views
    path('add/', add_product, name='add-product'),
    path('list/', product_list_view, name='product-list-view'),
    path('detail/<int:pk>/', product_detail_view, name='product-detail-view'),
]
