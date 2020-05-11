from django.urls import path

from .views import SalesCreate, SalesList,checkout,SalesDelete, SalesDetail, sales_update

app_name = 'sales'

urlpatterns = [
    path('',SalesList.as_view(), name = 'sale_list'),
    path('create/',SalesCreate.as_view(), name = 'sale_create'),
    path('payment/<pk>/<customer>/<order>/',checkout, name = 'sale_payment'),
    path('details/<pk>/<customer>/<order>/',SalesDetail.as_view(), name = 'sale_detail'),
    path('update/<pk>/<customer>/<order>/',sales_update, name = 'sale_update'),
    path('delete/<pk>/<customer>/<order>/',SalesDelete.as_view(), name = 'sale_delete')
]