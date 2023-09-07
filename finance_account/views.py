from django.views.generic import ListView, DetailView
from .models import FinanceAccount
from .forms import InputForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .budget_splitter import budget_splitter
from django.http import JsonResponse
import json

class UserListView(ListView):
    template_name = 'user_list.html'
    queryset = FinanceAccount.objects.all()
    context_object_name = 'accounts'

class UserDetail(DetailView):
    template_name = 'user_detail.html'
    queryset = FinanceAccount.objects.all()
    context_object_name = 'account'
    
def process_incomes(request):
    if request.method == 'POST':
        # Retrieve the JSON data sent by the client
        data = json.loads(request.body.decode('utf-8'))

        # Access the incomesData array
        incomes_data = data.get('incomesData', [])

        # Extract names, incomes, and expenses from the incoming data
        names = [entry['name'] for entry in incomes_data]
        incomes = [float(entry['income']) for entry in incomes_data]
        expenses = [float(entry['expense']) for entry in incomes_data]

        # Call your budget_splitter function to process the data
        processed_data = budget_splitter(names, incomes, expenses)

        # Return a JSON response with the processed data
        return JsonResponse({'processedData': processed_data})

    return JsonResponse({'error': 'Invalid request method'})

def new(request):
    if request.method == 'POST':
        income_names = request.POST.getlist('income_names')  
        incomes = request.POST.getlist('incomes')  

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

        return redirect('user_list')
    else:
        form = InputForm()
        
    context = {
        'form': form,
    }
    
    return render(request, 'base.html',context)



