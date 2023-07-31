from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Tender
from .forms import TenderForm
# Create your views here.

class TenderListView(ListView):
    model = Tender
    context_object_name = "tender_list"
    template_name = "tender/tender_list.html"

class TenderDetailView(DetailView):
    model = Tender
    context_object_name = "tender"
    template_name = "tender/tender_detail.html"

class TenderCreateView(CreateView):
    model = Tender
    fields = "__all__"
    template_name = "tender/tender_create.html"

class TenderUpdateView(UpdateView):
    pass


