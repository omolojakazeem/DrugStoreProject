import string
import random

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from .models import SalesOrder, OrderPayment
from .forms import SalesForm
from customer.models import Customer
from drug.models import DrugItem


def get_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


class SalesList(ListView):
    model = SalesOrder


class SalesDetail(DetailView):
    model = SalesOrder


class SalesDelete(DeleteView):
    model = SalesOrder
    success_url = reverse_lazy('sales:sale_list')


def sales_update(request, customer,pk,order):
    p_sales_order = SalesOrder.objects.get(customer__customer_last_name=customer)

    sales_form = SalesForm(data=request.POST or None, instance = p_sales_order)
    if sales_form.is_valid():
        sales_form.save()
        return redirect('sales:sale_list')
    context = {
        'order':p_sales_order,
        'form':sales_form,
    }
    return render(request, 'sale/salesitem_form.html', context=context)


class SalesCreate(View):

    def get(self, *args, **kwargs):
        form = SalesForm()
        context = {
            'form': form,
        }
        return render(self.request, 'sale/sales_create.html', context=context)

    def post(self, *args, **kwargs):
        form = SalesForm(self.request.POST or None)
        if form.is_valid():
            item = form.cleaned_data.get('item')
            customer = form.cleaned_data.get('customer')
            quantity = form.cleaned_data.get('quantity')

            p_customer = Customer.objects.get(customer_last_name=customer)
            if p_customer.customer_order_stat:
                # Customer has a pending order
                # 1. Delete
                # 2. Pay to clear
                print("You have a pending order")
                return redirect('sales:sale_list')
            else:

                order_item, created = SalesOrder.objects.get_or_create(
                    item=item,
                    customer=p_customer,
                    quantity=quantity,
                    ref_code=get_ref_code(),

                )
                p_customer.customer_order_stat = True
                p_customer.save()

                return redirect('sales:sale_list')


def checkout(request, customer, order, pk):
    order = SalesOrder.objects.get(customer__customer_last_name=customer)
    p_item = order.item
    p_customer = order.customer
    p_amount = order.get_total_order_price

    order_payment, created = OrderPayment.objects.get_or_create(
        customer=p_customer,
        order=order,
        amount=p_amount,
    )
    p_customer.customer_order_stat = False
    order.sold = True
    p_customer.save()
    order.save()
    return redirect('sales:sale_list')
