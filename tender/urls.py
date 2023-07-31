from django.urls import path
from .views import TenderListView, TenderDetailView, TenderCreateView

urlpatterns = [
    path("", TenderListView.as_view(), name="tender_list"),
    path("<uuid:pk>/", TenderDetailView.as_view(), name="tender_detail"),
    path("new-tender/", TenderCreateView.as_view(), name="tender_create"),
]