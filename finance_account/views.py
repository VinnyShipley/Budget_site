from .models import FinanceAccount
from .serializers import AccountSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

class UserListView(ListCreateAPIView):
  template_name = 'templates/user_list.html'
  queryset = FinanceAccount.objects.all()
  serializer_class = AccountSerializer
  context_object_name = 'accounts'

  
class UserDetail(RetrieveDestroyAPIView):
  queryset = FinanceAccount.objects.all()
  serializer_class = AccountSerializer
  context_object_name = 'accounts'

