from django.views.generic import ListView, DetailView
from .models import FinanceAccount
from .forms import UserInfoForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import json

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
        form = UserInfoForm(request.POST)
        if form.is_valid():
            # Serialize the list into a string
            income_names = json.dumps(form.cleaned_data['income_names'])
            
            finance_account = form.save(commit=False)
            finance_account.income_names = income_names
            finance_account.save()
            
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = UserInfoForm()
    return render(request, 'form.html', {'form': form})