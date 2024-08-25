from django.contrib import admin
from .models import Product,DateTest

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','active','category']
    list_display_links=['name','price']
    list_editable=['category','active']
    search_fields =['name']
    list_filter =['category']

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(DateTest)
admin.site.site_header='PRODUCT'
admin.site.site_title='product'
