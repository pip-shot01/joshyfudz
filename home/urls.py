from django.urls import path 
from . import views 
from . import views 
from . views import CheckoutView

urlpatterns = [
    path('',views.index, name='index'),
    path('contact',views.Contact, name='contact'),
    path('available_foods',views.products, name='products'),
    path('Signup', views.Register, name='register'),
    path('login_user', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile_update', views.profile_update, name='profile_update'),
    path('password', views.password, name='password'),
    path('shopcart', views.shopcart, name='shopcart'),
    path('displaycart', views.displaycart, name='displaycart'),
    path('deleteitem', views.deleteitem, name='deleteitem'),
    path('increase', views.increase, name='increase'),
    path('pay', views.pay, name='pay'),
    path('callback', views.callback, name='callback'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('details/<str:id>',views.details, name='details'),
]

