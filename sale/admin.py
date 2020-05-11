from django.contrib import admin
from .models import SalesOrder, OrderPayment


admin.site.register(SalesOrder)
admin.site.register(OrderPayment)
