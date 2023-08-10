# from .models import FinanceAccount
# from .serializers import AccountSerializer
# from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

# class UserListView(ListCreateAPIView):
#   template_name = 'templates/user_list.html'
#   queryset = FinanceAccount.objects.all()
#   serializer_class = AccountSerializer
#   context_object_name = 'accounts'

  
# class UserDetail(RetrieveDestroyAPIView):
#   queryset = FinanceAccount.objects.all()
#   serializer_class = AccountSerializer
#   context_object_name = 'accounts'

from django.views.generic import ListView, DetailView
from .models import FinanceAccount

class UserListView(ListView):
    template_name = 'user_list.html'
    queryset = FinanceAccount.objects.all()
    context_object_name = 'accounts'

class UserDetail(DetailView):
    template_name = 'user_detail.html'
    queryset = FinanceAccount.objects.all()
    context_object_name = 'account'

