from django.db import models
from django.urls import reverse
from drug.models import DrugItem
from customer.models import Customer


# Create your models here.
class SalesOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(DrugItem, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    sold = models.BooleanField(default=False)
    sales_date = models.DateTimeField(auto_now_add=True)
    ref_code = models.CharField(max_length=25, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('sales:sale_detail', kwargs={
            'pk': self.pk,
            'customer': self.customer,
            'order': self.__str__()
        })

    @property
    def get_total_order_price(self):
        return round(self.item.drug_price * self.quantity, 2)

    @property
    def get_delete_url(self):
        return reverse('sales:sale_delete', kwargs={
            'pk': self.pk,
            'customer':self.customer,
            'order':self.__str__()
        })

    def __str__(self):
        return f"{self.quantity} of {self.item.drug_name}"


class OrderPayment(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    order = models.ForeignKey(SalesOrder, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    payment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.get_full_name
