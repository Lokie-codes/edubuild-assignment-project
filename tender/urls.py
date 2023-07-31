from django.urls import path
from .views import TenderListView, TenderDetailView

urlpatterns = [
    path("", TenderListView.as_view(), name="tender_list"),
    path("<uuid:pk>/", TenderDetailView.as_view(), name="tender_detail"),
]