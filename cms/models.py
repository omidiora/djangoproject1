from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    profile_pic=models.CharField(max_length=200,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Indoor','indoor'),
         ('outdoor','out door'),
    )
    name=models.CharField(max_length=200)
    price=models.FloatField(max_length=200)
    category=models.CharField(max_length=200,choices=CATEGORY)
    description=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)
    tag=models.ManyToManyField(Tag)



    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(
        ('pending','pending'),
         ('out for delivery','out for delivery'),
         ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(Customer, null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=200,choices=STATUS)
    date_created=models.DateTimeField(auto_now_add=True)
    note=models.CharField(max_length=200)

    def __str__(self):
        return self.product.name
    
    

