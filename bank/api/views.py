from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from bank.models import Bank as BankModel
from .serializers import BankSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
# Create your views here.
# class Banklist(APIView):
#     def get (self,request):


#         Bank1=BankModel.objects.all()
#         serializer_class=BankSerializer(Bank1, many=True)
#         return Response(serializer_class.data)

@api_view(['GET'],)
def Banklist(request):
    Bank1=BankModel.objects.all()
    serializer_class=BankSerializer(Bank1, many=True)
    return Response(serializer_class.data)

class BankListView(ListAPIView):
    # def get(self,request):
    queryset=BankModel.objects.all()
    serializer_class=BankSerializer
    pagination_class=PageNumberPagination
        # return Response(serializer_class.data)
#     def post(self,request):
#         serializer_class= BankSerializer(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#         return Response(serializer_class.data, status=status.HTTP_201_CREATED)

# @api_view(['GET'],)
# def api_detail_bank_detail(request,slug):
#     try:
#         bank_detail=BankModel.objects.get(slug=slug)
#     except Bank.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)