from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("",views.index,name="Home"),
    path("items/",views.prod,name="item"),
    path('contactus', views.Contactus,name="contactus"),
    path('signup', views.handleSignup, name='signup'),
    path('getin', views.loginuser, name='getin'),
    path('getout', views.logoutuser, name='getout'),
    path('cart',views.Cart,name='cart'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('delete',views.delete,name='delete'),
    path('remove',views.remove,name='remove'),
    # path('balance',views.TotalBalance,name='balance'),
    path('totalbalance',views.deliverytotalprice,name='totalbalance'),
    path('checkout',views.delivery,name='checkout'),
    path('orderdelivery',views.delivertheorder,name='orderdelivery'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
urlpatterns += staticfiles_urlpatterns()