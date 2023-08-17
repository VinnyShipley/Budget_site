from django.views.generic import ListView, DetailView
from .models import FinanceAccount
from .forms import UserInfoForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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
        form.save
        return redirect('/')
    else:
        form = UserInfoForm()
    return render(request, 'form.html', {'form': form})