from django.contrib import admin

from .models import Customer 
from .models import Driver
from .models import Bus
from .models import Travel
from .models import DriverSalary

from string import ascii_lowercase

from django.db.models import Q

# Register your models here.

class AtoZFilter(admin.SimpleListFilter):
    title = 'A to Z Filter'
    parameter_name = 'letter'

    def lookups(self, request, model_admin):
        all_letter = []
        for letter in ascii_lowercase:
            inner  = (letter, letter)
            all_letter.append(inner)
        return tuple(all_letter)

    def queryset(self, request, queryset):
        if self.value() in list(ascii_lowercase):
            print(self.value())
            return queryset.filter( Q(name__contains= self.value()) )

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['admin_name', 'name', 'good', 'age', 'address', 'phone_number', 'job', 'factory']
    list_editable = ['good']
    list_filter = ['age', AtoZFilter]
    search_fields = ['name'] #or use __ to search in related fields
    ordering = ['age']
    fieldsets = (
        ('Personal Detail',{
            'fields':(
                ('name', 'username'),
                ('first_name', 'last_name'),
                ('address', 'age'),
            )
        }),
        ('job',{
            'classes':('collapse',),
            'fields':(
                'phone_number',
                'job',
                'factory',
            )
        })
    )

admin.site.register(Customer , CustomerAdmin )


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'first_name', 'last_name', 'joined_day']
    list_filter = ['joined_day']
    date_hierarchy = 'joined_day'
    fields = (
        ('name'),
        ('last_name' , 'first_name' ),
        ('address', 'age'),
        'phone_number',
        'holidays',
        'dependacy',   
    )
    save_as = True
    # save_on_top = True
    # radio_fields = {'featured': admin.HORIZONTAL}
    # filter_horizontal = ['field_name'] many to many field
    # prepopulated_fields = {'slug':('name',)}




def doubleSalary(model_admin, request, queryset):
    queryset.update(
        salary = 6000*2
    )
doubleSalary.short_description = 'Update Driver Salary with double'

class DriverSalaryAdmin(admin.ModelAdmin):
    actions = [doubleSalary]

admin.site.register(DriverSalary, DriverSalaryAdmin)



admin.site.register(Bus)
admin.site.register(Travel)
