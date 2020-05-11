from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import ExpensesForm
from .models import Expenses
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView


class ExpensesListView(ListView):
    model = Expenses


class ExpensesDetailView(DetailView):
    model = Expenses


class ExpensesUpdateView(UpdateView):
    model = Expenses
    form_class = ExpensesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'Update',
        })
        return context


class ExpensesCreateView(CreateView):
    model = Expenses
    form_class = ExpensesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'Create',
        })
        return context


class ExpensesDeleteView(DeleteView):
    model = Expenses
    success_url = reverse_lazy('expenses:expense_list')
