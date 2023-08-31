from django.urls import path
from .views import UserListView, UserDetail, input_form
from finance_account.views import new

urlpatterns = [
  path('', UserListView.as_view(), name='user_list'),
  path('accounts/<int:pk>', UserDetail.as_view(), name='user_detail'),
  path('form', new),
  path('input_form', input_form, name='input_form'),
]