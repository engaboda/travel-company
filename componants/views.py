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
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from .serializers import CustomerSerializer
from .serializers import DriverSerializer
from .serializers import TrvaleSerializer
from .serializers import BusSerializer
from .serializers import DriverSalarySerializer
from .serializers import MostPopularJobs
from .serializers import FactoryNumSerializer

from django.http import Http404

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'drivers': reverse('driver-list', request=request, format=format),
        'customers': reverse('customer-list', request=request, format=format),
        'jobs':reverse('most_popular_job', request=request, format=format),
        'factory':reverse('place_nums', request=request, format=format),
    })


class CustomerViewSet(viewsets.ModelViewSet):
    """
        list and create Customer 
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def job_nums_obj(self):
        '''
            return job name with num of them in table 
        '''
        try:
            job = Customer.objects.all().values('job','id')
            constract_query = []
            constarct_obj = {}
            for item in job:
                constarct_obj[ item.get('job') ] = constarct_obj.get( item.get('job'),0 )+1
                # constarct_obj['job'] = item.get('job')
                # constarct_obj['num'] = constarct_obj.get( item.get('job') )
            for k in constarct_obj:
                constract_query.append( {'job':k,'num':constarct_obj[k]} )
            # print(constract_query)
            return constract_query
        except Exception as e:
            return Http404

    def place_nums_obj(self):
        '''
        '''
        factory = Customer.objects.all().values('factory')
        constract_query = []
        constarct_obj = {}
        for item in factory:
            constarct_obj[ item.get('factory') ] = constarct_obj.get( item.get('factory'),0 )+1
        for k in constarct_obj:
            constract_query.append( {'factory':k,'num':constarct_obj[k]} )
        return constract_query


    def partial_job(self, job):
        """
            jobs that requested
        """
        cusomer_job = Customer.objects.filter(job=job)
        return cusomer_job


    @action(detail=False, method=['get'])
    def job_nums(self, request, format=None):
        '''
        '''
        customers = self.job_nums_obj()
        self.get_serializer_context().get('request').data['job']='eng'
        print(self.get_serializer_context())
        serializer = MostPopularJobs(customers, many=True , context=self.get_serializer_context() )
        return Response(serializer.data)

    def get_serializer_context(self, **kwargs):
        '''
        '''
        context = super(CustomerViewSet, self).get_serializer_context(**kwargs)
        context.update({
            'request':self.request,
        })
        return context

    @action(detail=False,method=['get'])
    def filter_job(self, request, job, format=None):
        '''
        '''
        customer = self.partial_job(job)
        serializer = CustomerSerializer(customer, many=True , context={'request':self.request})
        return Response(serializer.data)

    @action(detail=False, method=['get'] )
    def same_place(self, request, format=None):
        factory = self.place_nums_obj()
        serializer = FactoryNumSerializer(factory, many=True)
        return Response(serializer.data)
    
    def customer_factory(self,factory):
        places = Customer.objects.filter(factory=factory)
        return places
    
    @action(detail=False, method=['get'] )
    def filter_place_customer(self, request, factory, format=None):
        customer = self.customer_factory(factory)
        serializer = CustomerSerializer(customer, many=True , context={'request':self.request})
        return Response(serializer.data)


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