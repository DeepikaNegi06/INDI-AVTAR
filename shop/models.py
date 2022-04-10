from distutils.command.upload import upload
import types
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class color(models.Model):
    color_id = models.AutoField(primary_key=True)
    colors=models.CharField(max_length=50)

class categories(models.Model):
    fabric_types_id = models.AutoField(primary_key=True)
    fabric_types=models.CharField(max_length=60)

class Product(models.Model): 
    product_id = models.AutoField(primary_key=True)
    images = models.ImageField(upload_to = "img")
    price = models.CharField(max_length=20,null=False)
    description = models.TextField(max_length=200)
    numberofstock = models.IntegerField()
    color_id = models.ForeignKey(color,on_delete=models.CASCADE,default=1, verbose_name="colors")
    fabric_types_id = models.ForeignKey(categories,on_delete=models.CASCADE,default=1, verbose_name="fabric type")

   
    


class ShoppingCart(models.Model):
    Cart_id=models.AutoField(primary_key=True)
    user =models.ForeignKey(User,on_delete = models.CASCADE,default=1)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,default=1,  verbose_name="product_id")
    Quantity = models.IntegerField(max_length=10)
    Total_Bill = models.IntegerField(max_length=10)

class Wishlist(models.Model):
    user =models.ForeignKey(User,on_delete = models.CASCADE,default=1)
    Wishlist_id=models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,default=1,  verbose_name="product_id")
    
    # Cart_id=models.ForeignKey(Shopping_Cart,on_delete=models.CASCADE,default=1,  verbose_name="cart_id")

class Orders(models.Model):
    Order_Id=models.AutoField(primary_key=True)
    Delivery_Date=models.DateTimeField()
    Delivery_Address=models.TextField(max_length=200)
    Total_Bill = models.IntegerField(max_length=10)
    Cart_id=models.ForeignKey(ShoppingCart,on_delete=models.CASCADE,default=1,  verbose_name="cart_id")

class Payment_Gateway(models.Model):
    # FirstName=models.CharField(max_length=10)
    # LastName=models.CharField(max_length=10)
    # Delivery_Address=models.TextField(max_length=200)
    Transaction_Id=models.AutoField(primary_key=True)
    Payment_Method=models.CharField(max_length=10) 
    Phone_Number=models.CharField(max_length=10)
    # Order_Id=models.ForeignKey(Orders,on_delete=models.CASCADE,default=1,  verbose_name="order_id")


class Contact_us(models.Model):
     firstname = models.CharField(max_length=20)
     lastname= models.CharField(max_length=20)
     email = models.CharField(max_length=30)
     message = models.TextField(max_length=200)
    
     def __str__(self):
                return "Message from " + self.firstname +'-'+self.email



