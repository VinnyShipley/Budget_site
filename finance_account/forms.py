from django import forms

class InputForm(forms.Form):
    names = forms.CharField(label='Enter names (comma-separated)', widget=forms.TextInput(attrs={'placeholder': 'Name1, Name2, Name3'}))
    incomes = forms.CharField(label='Enter the incomes for the names (comma-separated)', widget=forms.TextInput(attrs={'placeholder': '1, 2, 3'}))
    expenses = forms.CharField(label='Enter the expenses for each incomes (comma-separated)', widget=forms.TextInput(attrs={'placeholder': '4, 5, 6'}))
