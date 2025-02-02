from django.shortcuts import render, redirect
from .models import Budget, Expense
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Income
from datetime import datetime
from django.db.models import Sum

from django.shortcuts import render, redirect
from .forms import IncomeForm, ExpenseForm

def index(request):
    budgets = Budget.objects.all()
    return render(request, 'index.html', {'budgets': budgets})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')

def user_registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            messages.success(request, "Registration successful. Welcome!")
            return redirect('login')  # Redirect to dashboard after successful registration
        else:
            messages.error(request, "Error in registration. Please check the form.")
    else:
        form = RegisterForm()
    
    return render(request, 'registration.html', {'form': form})

def user_dash(request):
    return render(request, 'dashboard.html')


def expense(request):
    return render(request, 'about.html')
"""
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BudgetForm()
    return render(request, 'add_budget.html', {'form': form})

def add_expense(request, budget_id):
    budget = Budget.objects.get(id=budget_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.budget = budget
            expense.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form, 'budget': budget})
"""

from django.shortcuts import render, redirect
from .forms import IncomeForm, ExpenseForm

from django.shortcuts import render, redirect
from .forms import IncomeForm, ExpenseForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Initialize both forms first
    income_form = IncomeForm()
    expense_form = ExpenseForm()

    # Query the database to get all income and expense records for the logged-in user
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    if request.method == 'POST':
        if 'add_income' in request.POST:  # Check if it's the Income form
            income_form = IncomeForm(request.POST)
            if income_form.is_valid():
                # Save the Income form with the logged-in user
                income = income_form.save(commit=False)
                income.user = request.user  # Assign the logged-in user
                income.save()
                return redirect('dashboard')  # Redirect after successful form submission
        elif 'add_expense' in request.POST:  # Check if it's the Expense form
            expense_form = ExpenseForm(request.POST)
            if expense_form.is_valid():
                # Save the Expense form with the logged-in user
                expense = expense_form.save(commit=False)
                expense.user = request.user  # Assign the logged-in user
                expense.save()
                return redirect('dashboard')  # Redirect after successful form submission

    return render(request, 'dashboard.html', {
        'income_form': income_form,
        'expense_form': expense_form,
        'incomes': incomes,  # Pass the user's income records
        'expenses': expenses,  # Pass the user's expense records
    })