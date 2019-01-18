from django.urls import path, include

from .views import CustomerViewSet
from .views import DriverList
from .views import DriverDetail
from .views import api_root
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()

customers_list = CustomerViewSet.as_view({
    'get':'list',
    'post':'create',
})
customers_detail = CustomerViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'path':'partial_update',
    'delete':'destroy',
})




urlpatterns = [
    path('',  api_root),
    path('customer/',customers_list,name='customer-list'),
    path('customer/<int:pk>/',customers_detail,name='customer-detail'),
    path('drivers/', DriverList.as_view(), name='driver-list'),
    path('drivers/<int:pk>/', DriverDetail.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)