from django.urls import path
from bank.api.views import BankListView, Banklist

app_name = 'bank'

urlpatterns = [
    path('', Banklist, name='bank-list'),
    path('list/',BankListView.as_view(),name="list")
]