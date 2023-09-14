from django.urls import path
from finance_account.views import new
from .views import UserListView
from . import views

urlpatterns = [
  path('', new, ),
  path('user_list/', UserListView.as_view(), name='user_list'),
  path('process_incomes/', views.process_incomes, name='process_incomes'),
]