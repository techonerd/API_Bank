from rest_framework import serializers
from bank.models import Bank

class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        # can't create ModelSerializers without fields
        fields = '__all__'