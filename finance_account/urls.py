from django.urls import path
from .views import UserListView, UserDetail, input_form
from finance_account.views import new

urlpatterns = [
  path('', new, ),
  path('accounts/<int:pk>', UserDetail.as_view(), name='user_detail'),
  path('input_form', input_form, name='input_form'),
]