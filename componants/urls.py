from django.urls import path, include
from django.conf.urls import url

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
most_popular = CustomerViewSet.as_view({
    'get':'job_nums',
})
place_nums = CustomerViewSet.as_view({
    'get':'same_place'
})
customer_job = CustomerViewSet.as_view({
    'get':'filter_job',
})

customer_places = CustomerViewSet.as_view({
    'get':'filter_place_customer',
})


urlpatterns = [
    path('',  api_root),
    path('customer/',customers_list,name='customer-list'),
    path('customer/jobs/', most_popular ,name='most_popular_job'),
    url(r'customer/jobs/(?P<job>[\w\-]+)/', customer_job ,name='customer_job'),
    path('customer/factory/', place_nums ,name='place_nums'),
    url(r'customer/factory/(?P<factory>[\w\-]+)/', customer_places ,name='customer_factory'),
    path('customer/<int:pk>/',customers_detail,name='customer-detail'),
    path('drivers/', DriverList.as_view(), name='driver-list'),
    path('drivers/<int:pk>/', DriverDetail.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)