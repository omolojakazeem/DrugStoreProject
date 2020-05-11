from django.db import models

# Create your models here.
from customer.models import Customer
from django.urls import reverse

from drug.models import User


class ExpensesCat(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Expenses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(ExpensesCat, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    spent_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('expenses:expense_detail', kwargs={
            'exp_cat':self.category,
            'exp_title': self.title,
            'pk':self.pk,
        })


    def __str__(self):
        return self.title