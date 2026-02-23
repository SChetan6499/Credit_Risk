from django.urls import path
from .views import apply_loan

urlpatterns = [
    path("", apply_loan, name="apply_loan"),
]
