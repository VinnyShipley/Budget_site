from rest_framework import serializers
from .models import FinanceAccount

class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('username', 'income', 'expenses')
    model = FinanceAccount