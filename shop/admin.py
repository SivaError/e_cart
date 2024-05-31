from django.contrib import admin
from . models import *


class CatagoryAdmin(admin.ModelAdmin):
    list_display=('name','image',)
admin.site.register(Catagory,CatagoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','image','description')
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)

