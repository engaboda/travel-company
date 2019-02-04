from .models import Customer 
from .models import Driver
from .models import Bus
from .models import Travel
from .models import DriverSalary

from rest_framework import serializers
from rest_framework.reverse import reverse

class CustomerSerializer(serializers.ModelSerializer):
    uri = serializers.HyperlinkedIdentityField(view_name='customer-detail',format='html')
    class Meta:
        model = Customer
        fields = ('uri', 'name', 'username', 'first_name', 'last_name', 'address', 'age', 'phone_number', 'job', 'factory' )
        read_only_fields= ('name',)

class CustomHyperLink(serializers.HyperlinkedRelatedField):
    view_name='customer_job'
    queryset = Customer.objects.all()
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'job':obj.job,
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)
    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs ={
            'job':view_kwargs['job'],
        }
        return self.get_queryset().get(**lookup_kwargs)



class MostPopularJobs(serializers.Serializer):
    # uri = serializers.HyperlinkedIdentityField(view_name='customer_job', format='html', lookup_field='job')
    job = serializers.CharField(max_length=100)
    num = serializers.IntegerField()

    # class Meta:
        # model = Customer
        # fields = ('job','num','uri')

class FactoryNumSerializer(serializers.Serializer):
    # uri = serializers.HyperlinkedIdentityField(view_name='customer_job', format='html')
    factory = serializers.CharField(max_length=100)
    num = serializers.IntegerField()
    # class Meta:
    #     model = Customer
    #     fields = ('factory','num')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'name', 'username', 'first_name', 'last_name', 'address', 'age', 'phone_number', 'holidays', 'dependacy', 'joined_day' )


class TrvaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ('driver', 'customer', 'bus', 'f_place', 't_place', 'esti_time', 'gas')

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('owner', 'Driver', 'code')

class DriverSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverSalary
        fields = ('driver', 'date', 'salary', 'promo')