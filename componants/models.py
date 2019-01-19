from django.db import models

# Create your models here.

class AbstractModel(models.Model):
    """
        
    """    
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)

    def save(self, *args, **kwargs):
        self.name = self.first_name + " " + self.last_name
        super().save(*args,**kwargs)
    
    class Meta:
        abstract = True

class Customer(AbstractModel):
    """
        Model for our users
    """
    job = models.CharField(max_length=100)
    factory = models.CharField(max_length=100)

    def __str__(self):
        return self.name  

class Driver(AbstractModel):
    """
        Driver for our company
    """
    holidays = models.CharField(max_length=7, choices={('fri-sat','Friday and Satrday'),('thu-fri','Friday and Thursday')})
    dependacy = models.IntegerField()
    joined_day = models.DateField(auto_now_add=True)
    driversalary = models.ForeignKey('DriverSalary', related_name='driver_salary', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Bus(models.Model):
    owenr = models.CharField(max_length=100)
    code = models.IntegerField()
    Driver = models.ManyToManyField(Driver, related_name='driver_bus')

class Travel(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver_travel')
    customer = models.ManyToManyField(Customer, related_name='customers_travel')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='travel_bus')
    f_place = models.CharField(max_length=100)
    t_place = models.CharField(max_length=100)
    esti_time = models.TimeField(auto_now=False)
    gas = models.DecimalField(max_digits=100,decimal_places=3)
    s_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return 


class DriverSalary(models.Model):
    date = models.DateField(auto_now_add=True)
    salary = models.IntegerField()
    promo = models.IntegerField()

    def __str__(self):
        return self.driver.name