from django.urls import path
from finance_account.views import new

urlpatterns = [
  path('', new, ),
]