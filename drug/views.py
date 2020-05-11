from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import DrugItem
from .forms import DrugItemForm


class DrugListView(ListView):
    model = DrugItem


class DrugCreateView(CreateView):
    model = DrugItem
    form_class = DrugItemForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


class DrugDetailView(DetailView):
    model = DrugItem


class DrugUpdateView(UpdateView):
    model = DrugItem
    form_class = DrugItemForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context


class DrugDeleteView(DeleteView):
    model = DrugItem
    success_url = reverse_lazy('drugs:drug_list')
