from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from bank.models import Bank as BankModel
from .serializers import BankSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view


@api_view(['GET'],)
def Banklist(request):
    # returning all data now, will implement search funtionality later.
    Bank1=BankModel.objects.all().order_by('id')
    serializer_class=BankSerializer(Bank1, many=True)
    return Response(serializer_class.data)

# classed based view with pagination
class BankListView(ListAPIView):
    queryset=BankModel.objects.all().order_by('id')
    serializer_class=BankSerializer
    pagination_class=PageNumberPagination

# @api_view(['GET'],)
# def api_detail_bank_detail(request,slug):
#     try:
#         bank_detail=BankModel.objects.get(slug=slug)
#     except Bank.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
        # return Response(serializer_class.data)
#     def post(self,request):
#         serializer_class= BankSerializer(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#         return Response(serializer_class.data, status=status.HTTP_201_CREATED)