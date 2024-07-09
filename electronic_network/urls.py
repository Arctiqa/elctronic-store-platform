from electronic_network.apps import ElectronicNetworkConfig
from django.urls import path

from electronic_network.views.node import NodeCreateAPIView, NodeListAPIView, NodeUpdateAPIView, NodeDestroyAPIView, \
    NodeDetailAPIView

app_name = ElectronicNetworkConfig.name

urlpatterns = [
    path('', NodeListAPIView.as_view(), name='list'),
    path('create/', NodeCreateAPIView.as_view(), name='create'),
    path('update/<int:pk>/', NodeUpdateAPIView.as_view(), name='update'),
    path('detail/<int:pk>/', NodeDetailAPIView.as_view(), name='detail'),
    path('delete/<int:pk>/', NodeDestroyAPIView.as_view(), name='delete'),


]