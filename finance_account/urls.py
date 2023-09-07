from django.urls import path
from finance_account.views import new
from .views import UserListView

urlpatterns = [
  path('', new, ),
  path('user_list/', UserListView.as_view(), name='user_list'),
]