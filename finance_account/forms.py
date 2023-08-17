from .models import FinanceAccount
from django.forms import ModelForm

class UserInfoForm(ModelForm):
  class Meta:
    model = FinanceAccount
    fields = '__all__'