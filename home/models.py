from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    messages = models.TextField()
    time_received = models.DateTimeField(auto_now_add=True)
    admin_note = models.CharField(max_length=50, default='4')
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'Contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

class Product(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to= 'Product', default='prod.jpg')
    price = models.CharField(max_length=100)
    max_quantity = models.IntegerField()
    min_quantity = models.IntegerField(default=1, editable=False)
    display = models.BooleanField()
    latest = models.BooleanField(default=False)
    trending =models.BooleanField(default=False)
    meals =models.BooleanField(default=False)
    wines =models.BooleanField(default=False)
    snacks =models.BooleanField(default=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    username = models.CharField(max_length=50, default='a')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)  #editable=False
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pix = models.ImageField(upload_to= 'profile', default= 'download.jpg')
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'Profile'
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class Shopcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name_id = models.CharField(max_length=50,default='a')
    quantity = models.IntegerField()
    price = models.IntegerField()
    amount = models.IntegerField(blank= True, null=True)
    order_no = models.CharField(max_length=250)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.name
    
    
