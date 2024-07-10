from electronic_network.apps import ElectronicNetworkConfig
from django.urls import path

from electronic_network.views.contacts import ContactsListAPIView, ContactsDestroyAPIView, ContactsDetailAPIView, \
    ContactsUpdateAPIView, ContactsCreateAPIView
from electronic_network.views.supplier import SupplierCreateAPIView, SupplierListAPIView, SupplierUpdateAPIView, SupplierDestroyAPIView, \
    SupplierDetailAPIView
from electronic_network.views.product import ProductListAPIView, ProductCreateAPIView, ProductUpdateAPIView, \
    ProductDetailAPIView, ProductDestroyAPIView

app_name = ElectronicNetworkConfig.name

urlpatterns = [
    path('', SupplierListAPIView.as_view(), name='list'),
    path('create/', SupplierCreateAPIView.as_view(), name='create'),
    path('update/<int:pk>/', SupplierUpdateAPIView.as_view(), name='update'),
    path('detail/<int:pk>/', SupplierDetailAPIView.as_view(), name='detail'),
    path('delete/<int:pk>/', SupplierDestroyAPIView.as_view(), name='delete'),

    path('contacts/', ContactsListAPIView.as_view(), name='contacts-list'),
    path('contacts/create/', ContactsCreateAPIView.as_view(), name='contacts-create'),
    path('contacts/update/<int:pk>/', ContactsUpdateAPIView.as_view(), name='contacts-update'),
    path('contacts/detail/<int:pk>/', ContactsDetailAPIView.as_view(), name='contacts-detail'),
    path('contacts/delete/<int:pk>/', ContactsDestroyAPIView.as_view(), name='contacts-delete'),

    path('products/', ProductListAPIView.as_view(), name='products-list'),
    path('products/create/', ProductCreateAPIView.as_view(), name='products-create'),
    path('products/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='products-update'),
    path('products/detail/<int:pk>/', ProductDetailAPIView.as_view(), name='products-detail'),
    path('products/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='products-delete'),

]
