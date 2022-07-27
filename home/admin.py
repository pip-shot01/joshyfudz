from django.contrib import admin
# from . models import Contact,Product,Profile
from . models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email','messages','admin_note','last_name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','meals','wines','snacks','img','price','max_quantity','min_quantity','display','latest','trending','description','created','update']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','username','first_name','last_name','email','phone','address','state','pix']
    
class ShopcartAdmin(admin.ModelAdmin):
     list_display = ['id','user','product','quantity','price','amount','order_no','paid','created_at']

admin.site.register(Contact,ContactAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Shopcart,ShopcartAdmin)