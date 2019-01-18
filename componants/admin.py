from django.contrib import admin

from .models import Customer 
from .models import Driver
from .models import Bus
from .models import Travel
from .models import DriverSalary

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ['name']

admin.site.register(Customer , CustomerAdmin )
admin.site.register(Driver)
admin.site.register(Bus)
admin.site.register(Travel)
admin.site.register(DriverSalary)
