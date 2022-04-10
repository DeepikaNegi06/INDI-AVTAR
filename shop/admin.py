from django.contrib import admin

# Register your models here.
from .models import color,categories, Product,ShoppingCart, Wishlist, Orders, Payment_Gateway, Contact_us
admin.site.register (color)
admin.site.register (categories)

admin.site.register (Product)

admin.site.register (ShoppingCart)
admin.site.register (Wishlist)
admin.site.register (Orders)
admin.site.register (Payment_Gateway)
admin.site.register (Contact_us)

class imageadmin(Product):
    list_display=['product_id', 'images', 'price', 'description', 'color', 'numberofstock', 'category']
