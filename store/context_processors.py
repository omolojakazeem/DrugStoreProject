from customer.models import Customer
from drug.models import DrugItem
from sale.models import SalesOrder
from expenses.models import Expenses


def common(request):
    try:
        total_drugs = DrugItem.objects.all()
        total_customers = Customer.objects.all()
        total_orders = SalesOrder.objects.all()
        total_expenses = Expenses.objects.all()

        context = {
            'total_drugs': total_drugs,
            'total_customers': total_customers,
            'total_orders': total_orders,
            'total_expenses': total_expenses,
        }

    except:
        context = 0

    return context
