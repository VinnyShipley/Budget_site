from django.urls import path
from .views import UserListView, UserDetail

urlpatterns = [
  path('', UserListView.as_view(), name='user_list'),
  path('accounts/<int:pk>', UserDetail.as_view(), name='user_detail')
]