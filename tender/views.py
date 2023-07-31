from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Tender

# Create your views here.

class TenderListView(ListView):
    model = Tender
    context_object_name = "tender_list"
    template_name = "tender/tender_list.html"

class TenderDetailView(DetailView):
    model = Tender
    context_object_name = "tender"
    template_name = "tender/tender_detail.html"