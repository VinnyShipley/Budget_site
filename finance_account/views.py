from django.views.generic import ListView, DetailView
from .models import FinanceAccount
from .forms import UserInfoForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import json
from django.contrib.auth import get_user_model

class UserListView(ListView):
    template_name = 'user_list.html'
    queryset = FinanceAccount.objects.all()
    context_object_name = 'accounts'

class UserDetail(DetailView):
    template_name = 'user_detail.html'
    queryset = FinanceAccount.objects.all()
    context_object_name = 'account'

def new(request):
    if request.method == 'POST':
        income_names = request.POST.getlist('income_names')  # Replace with the actual field name
        incomes = request.POST.getlist('incomes')  # Replace with the actual field name

        income_names_str = '{{{}}}'.format(', '.join('"{}"'.format(item) for item in income_names))
        incomes_str = '{{{}}}'.format(', '.join(str(item) for item in incomes))

        user = get_user_model().objects.get(username=request.user.username)

        finance_account = FinanceAccount(
            owner=user,
            income_names=income_names_str,
            incomes=incomes_str,
            # other fields...
        )
        finance_account.save()

        # Redirect or render success page here
    else:
        # Handle GET request
        return render(request, 'your_template.html', context)