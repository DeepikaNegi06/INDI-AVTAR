from urllib import request
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, color, categories,Orders

from pickle import NONE
from django.shortcuts import redirect, render, get_object_or_404
from shop.models import Contact_us
from shop.models import ShoppingCart,Wishlist
from django.core.mail import send_mail
from django.contrib.auth.models import User,auth
from django.conf import settings
from django.contrib.auth import authenticate, login, logout


products= Product.objects.all()
# col = color.objects.all()
# cat = categories.objects.all()
data={'products':products}
# content={'color':col}
# itm={'categories':cat}

def index(request):
    return render(request,'shop/index.html',data)

def prod(request):    
    return render(request,'shop/items.html',data)

def Contactus(request ): 

     if request.method=='POST':
          firstname=request.POST.get('fname')
          lastname=request.POST.get('lname')
          email=request.POST.get('emailid')
          subject=request.POST.get('subject')
          message=request.POST.get('messages') 
          
          dataa = {
               'firstname':firstname,
               'lastname':lastname,
               'email':email,
               'subject':subject,
               'message':message
          }
          contact = Contact_us(firstname=firstname, lastname=lastname,email=email,message=message)
          contact.save()
 
          
          # emailid = EmailMessage('Subject', message, settings.EMAIL_HOST_USER, to=[email])
          # emailid.send()
          # send_mail('subject',message, settings.EMAIL_HOST_USER, email)
          message='''
          New Message: {}
          
          FROM: {}
          
          
          '''.format(dataa['message'], dataa['email'])
          send_mail(dataa['subject'],message, '', ['indiefashionnew@gmail.com'])
     return render(request, 'shop/contactus.html')
      
def handleSignup(request):

     if request.method == 'POST':
          # get the post perameters

          username = request.POST.get('username')
          
          email=request.POST.get('email')
        #   myuser = CustomerDetails(fname=fname, lname=lname,email=email,state=state,Address=Address,city=city,Pincode=Pincode)
        #   myuser.save()
          
          if User.objects.filter(email=email).exists():
            return render(request, 'shop/createaccount.html', {'error': 'Email already exists'})
          else:
            try:
                password = request.POST.get('pswd')
                password_c = request.POST.get('pswrepeat')
                if password == password_c:
                    user = User.objects.create_user(
                        username=username, email=email, password=password)
                    user.save()
                    
                    login(request, user)
                    return render(request, 'shop/login.html', {'name': username, 'email': email})
                else:
                    return render(request, 'shop/createaccount.html', {'error': 'Incorrect Password'})
            except IntegrityError:
                return render(request, 'shop/createacccount.html', {'error': 'Username already exists'})
          
     return render(request,'shop/createaccount.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pswd')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            return render(request, 'shop/login.html', {'error': 'Invalid Username or Password'})
    return render(request, 'shop/login.html')

def logoutuser(request):
    logout(request)
    return redirect('Home')

def Cart(request):
     cart = ShoppingCart.objects.all()
     total=0
     if request.method=='POST':   
          product_id=request.POST.get('product_id')
          Quantity=request.POST.get('qty')
          price=request.POST.get('price')
          products = get_object_or_404(Product, product_id=product_id)
          usr = get_object_or_404(User, id=request.user.id)
          c= ShoppingCart(product_id=products, Quantity=Quantity, Total_Bill=price, user=usr)
          c.save()
          return render(request,'shop/Cart.html', {'cart':cart})
     for i in cart:
          total=total+i.Total_Bill
     grand=total+(total*0.10)
     return render(request, 'shop/Cart.html', {'cart':cart, 'total':total, 'grand':grand})

def deliverytotalprice(request):
     cart = ShoppingCart.objects.all()
     total=0
     if request.method=='POST':   
          Delivery_Address=request.POST.get('Delivery_Address')
          Quantity=request.POST.get('qty')
          price=request.POST.get('price')
          usr = get_object_or_404(User, id=request.user.id)
          c= ShoppingCart(product_id=products, Quantity=Quantity, Total_Bill=price, user=usr)
          c.save()
          payment = Orders(Delivery_Address=Delivery_Address)
          payment.save()
          # return render(request, 'shop/Checkout.html')
          return render(request,'shop/Cart.html', {'cart':cart})

     for i in cart:
          total=total+i.Total_Bill
     grand=total+(total*0.10)
     return render(request, 'shop/Cart.html', {'cart':cart, 'total':total, 'grand':grand})



# def TotalBalance(request):
#      cart = ShoppingCart.objects.all()
#      total=0
#      if request.method=='POST':
#                product_id=request.POST.get('product_id')
#                Quantity=request.POST.get('qty')
#                price=request.POST.get('price')
#                products = get_object_or_404(Product, product_id=product_id)
#                usr = get_object_or_404(User, id=request.user.id)
#                c= ShoppingCart(product_id=products, Quantity=Quantity, Total_Bill=price, user=usr)
#                c.save()
#                return render(request,'shop/Cart.html', {'cart':cart})
#      for i in cart:
#           total=total+i.Total_Bill
#      grand=total+(total*0.10)
#      return render(request, 'shop/Cart.html', {'cart':cart, 'total':total, 'grand':grand})
     # return redirect('checkout')








# def TotalBalance(request):
#      cart = ShoppingCart.objects.all()
#      total=0
#      if request.method=='POST':
#                product_id=request.POST.get('product_id')
#                Quantity=request.POST.get('qty')
#                price=request.POST.get('price')
#                products = get_object_or_404(Product, product_id=product_id)
#                usr = get_object_or_404(User, id=request.user.id)
#                c= ShoppingCart(product_id=products, Quantity=Quantity, Total_Bill=price, user=usr)
#                c.save()
#                return render(request,'shop/Cart.html', {'cart':cart})
#      for i in cart:
#           total=total+i.Total_Bill
#      grand=total+(total*0.10)
#      return render(request, 'shop/Cart.html', {'cart':cart, 'total':total, 'grand':grand})

def delete(request):
     id=request.POST.get('id')
     ShoppingCart.objects.filter(Cart_id=id).delete()
     return redirect('cart')
     

def wishlist(request):
     wishlist = Wishlist.objects.all()
     if request.method=='POST':   
          product_id=request.POST.get('product_id')
          usr = get_object_or_404(User, id=request.user.id)
          # Cart_id=request.POST.get('cart_id')
          products = get_object_or_404(Product, product_id=product_id )
          
          c= Wishlist(product_id=products,user=usr)
          c.save()
          return render(request,'shop/Wishlist.html',{'wishlist':wishlist})
     return render(request, 'shop/Wishlist.html', {'wishlist':wishlist})

def remove(request):
     id=request.POST.get('id')
     Wishlist.objects.filter(Wishlist_id=id).delete()
     return redirect('wishlist')

# def delivery(request):
#      if request.method=='POST':
#           # FirstName=request.POST.get('FirstName')
#           # LastName=request.POST.get('LastName')
#           Delivery_Address=request.POST.get('Delivery_Address')
          

#           payment = Orders(Delivery_Address=Delivery_Address)
#           payment.save()

#      return render(request, 'shop/Checkout.html')

# cart = ShoppingCart.objects.all()
# total=0
# for i in cart:
#      total=total+i.Total_Bill
#      grand=total+(total*0.10)
# print(grand)
# def deliverytotalprice(request):
#      cart = ShoppingCart.objects.all()
#      total=0
#      if request.method=='POST':   
#           Delivery_Address=request.POST.get('Delivery_Address')
#           Quantity=request.POST.get('qty')
#           price=request.POST.get('price')
#           usr = get_object_or_404(User, id=request.user.id)
#           c= ShoppingCart(product_id=products, Quantity=Quantity, Total_Bill=price, user=usr)
#           c.save()
#           payment = Orders(Delivery_Address=Delivery_Address)
#           payment.save()
#           # return render(request, 'shop/Checkout.html')
#           return render(request,'shop/Cart.html', {'cart':cart})

#      for i in cart:
#           total=total+i.Total_Bill
#      grand=total+(total*0.10)
#      return render(request, 'shop/Cart.html', {'cart':cart, 'total':total, 'grand':grand})

# def TotalBalance(request):
#      cart = ShoppingCart.objects.all()
#      total=0
#      if request.method=='POST':
#                product_id=request.POST.get('product_id')
#                Quantity=request.POST.get('qty')
#                price=request.POST.get('price')
#                products = get_object_or_404(Product, product_id=product_id)
#                usr = get_object_or_404(User, id=request.user.id)
#                c= ShoppingCart(product_id=products, Quantity=Quantity, Total_Bill=price, user=usr)
#                c.save()
#                return render(request,'shop/Cart.html', {'cart':cart})
#      for i in cart:
#           total=total+i.Total_Bill
#      grand=total+(total*0.10)
#      return render(request, 'shop/Cart.html', {'cart':cart, 'total':total, 'grand':grand})
#      # return redirect('checkout')




# total=0
# for i in Cart:
#      print(total)

# for i in delivery:
     # delivery = Cart()
     # total=total+i.Total_Bill
     # grand=total+(total*0.10)
     # return render(request, 'shop/Checkout.html')
     #  return redirect('checkout')



          # dictinory = {
          # 'FirstName':FirstName,
          # 'LastName':LastName,
          # 'Delivery_Address':Delivery_Address,
               
          # }

# def ordered(request):
#      if request.method=='POST':
#           # FirstName=request.POST.get('FirstName')
#           # LastName=request.POST.get('LastName')
#           return render(request, 'shop/orderdelivery.html')


# def deliverytotalprice(request):
#      cart = ShoppingCart.objects.all()
#      total=0
#      if request.method=='POST':   
#           Delivery_Address=request.POST.get('Delivery_Address')
#           Quantity=request.POST.get('qty')
#           price=request.POST.get('price')
#           usr = get_object_or_404(User, id=request.user.id)
#           c= ShoppingCart(product_id=products, Quantity=Quantity, Total_Bill=price, user=usr)
#           c.save()
#           payment = Orders(Delivery_Address=Delivery_Address)
#           payment.save()
#           # return render(request, 'shop/Checkout.html')
#           return render(request,'shop/Cart.html', {'cart':cart})

#      for i in cart:
#           total=total+i.Total_Bill
#      grand=total+(total*0.10)
#      return render(request, 'shop/Cart.html', {'cart':cart, 'total':total, 'grand':grand})

def delivery(request):
     if request.method=='POST':
          # FirstName=request.POST.get('FirstName')
          # LastName=request.POST.get('LastName')
          Delivery_Address=request.POST.get('Delivery_Address')
          

          payment = Orders(Delivery_Address=Delivery_Address)
          payment.save()
     return render(request, 'shop/Checkout.html')

def delivertheorder(request):
     if request.method=='POST':
          return redirect('orderdelivery')
