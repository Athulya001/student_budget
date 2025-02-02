from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # password1 = password, password2 = confirm password
        
from django import forms
from .models import Income, Expense

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount']  # Include only fields you want to show in the form

    # Optionally, you can add custom validation or widgets here if needed.

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'reason', 'date_spent']  # Include the fields to show in the form

    # You can also customize the widget for `date_spent` to display a date picker:
    date_spent = forms.DateField(widget=forms.SelectDateWidget())


