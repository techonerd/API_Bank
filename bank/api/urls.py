from django.urls import path
from bank.api.views import BankListView, Banklist

app_name = 'bank'

urlpatterns = [
    path('bank/', Banklist, name='bank-list'),
    path('bank/list/',BankListView.as_view(), name="list") # paginated response
]