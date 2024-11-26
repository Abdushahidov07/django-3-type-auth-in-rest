from django.db import models

# Create your models


class Company(models.Model):
    name_company = models.CharField(max_length=50)
    description =  models.TextField()
    profit = models.DecimalField(max_digits=8, decimal_places=2)
    date_birth = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name_company


class Car(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.IntegerField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    probeg = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField( auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.car_name



