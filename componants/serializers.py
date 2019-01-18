from .models import Customer 
from .models import Driver
from .models import Bus
from .models import Travel
from .models import DriverSalary

from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'username', 'first_name', 'last_name', 'address', 'age', 'phone_number', 'job', 'factory' )
        read_only_fields= ('name',)
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