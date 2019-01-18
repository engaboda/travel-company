from django.shortcuts import render

from .models import Customer 
from .models import Driver
from .models import Bus
from .models import Travel
from .models import DriverSalary

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.reverse import reverse

from .serializers import CustomerSerializer
from .serializers import DriverSerializer
from .serializers import TrvaleSerializer
from .serializers import BusSerializer
from .serializers import DriverSalarySerializer

from django.http import Http404

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'drivers': reverse('driver-list', request=request, format=format),
        'customers': reverse('customer-list', request=request, format=format)
    })


class CustomerViewSet(viewsets.ModelViewSet):
    """
        list and create Customer 
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DriverList(APIView):
    """
        list and create Driver
    """
    @classmethod
    def get_extra_actions(cls):
        return []
    def get(self, request, format=None ):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request , format=None ):
        data = request.data
        serializer = DriverSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DriverDetail(APIView):
    '''
        detail or update or retrieve
    '''
    def get_object(self, pk):
        try:
            driver = Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            return Http404
    
    def get(self, request, pk , format=None):
        data = self.get_object(pk)
        serializer = DriverSalarySerializer(data=data)
        return Response(serializer.data)
    
    def put(self, request, pk , format=None ):
        driver = self.get_object(pk)
        data = request.data
        serializer = DriverSerializer(driver, data=data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None ):
        driver = self.get_object(pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)