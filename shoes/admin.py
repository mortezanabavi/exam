from django.contrib import admin
from shoes.models import Order, Product
from rest_framework.authtoken.models import TokenProxy
admin.site.unregister(TokenProxy)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "stock", "get_price"]
    search_fields = ["name", "stock"]

    def get_price(self, obj):
        return "{:,} تومان".format(obj.price)

    get_price.short_description = "قیمت محصول"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "status", "get_pr"]
    search_fields = ["user", "status"]

    def get_pr(self, obj):
        return "{:,} تومان".format(obj.full_price)

    get_pr.short_description = "جمع کل سفارش"