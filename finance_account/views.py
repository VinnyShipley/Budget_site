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


def input_form(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            num_incomes = int(form.cleaned_data['num_incomes'])
            names = form.cleaned_data['names'].split(', ')
            single_values = form.cleaned_data['incomes'].split(', ')

            multi_values = []
            for i in range(num_incomes):
                expense_key = f'expenses_{i + 1}'
                multi_values.append(form.cleaned_data.get(expense_key, ''))

            # Process the form data and call budget_splitter function
            incomes = [int(value) for value in single_values]
            expenses = [
                list(map(int, values.split(', '))) if values else []
                for values in multi_values
            ]
            results = budget_splitter(names, incomes, expenses)

            context = {
                'form': form,
                'results': results,
            }
            return render(request, 'base.html', context)
    else:
        form = InputForm()

    context = {
        'form': form,
    }
    return render(request, 'base.html', context)

