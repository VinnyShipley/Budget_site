from django import forms

class InputForm(forms.Form):
    num_incomes = forms.IntegerField(label='Enter the number of incomes')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_bound:
            num_incomes = self.cleaned_data.get('num_incomes', 0)
            for i in range(num_incomes):
                self.fields[f'income_{i+1}'] = forms.DecimalField(label=f'Income {i+1}', required=False)
                self.fields[f'expenses_{i+1}'] = forms.CharField(label=f'Expenses for Income {i+1}', widget=forms.TextInput(attrs={'placeholder': '4, 5, 6'}))

    def clean_num_incomes(self):
        num_incomes = self.cleaned_data.get('num_incomes')
        if num_incomes <= 0:
            raise forms.ValidationError("Number of incomes must be greater than 0")
        return num_incomes

