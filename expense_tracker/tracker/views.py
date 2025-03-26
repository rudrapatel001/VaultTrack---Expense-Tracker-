from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ExpenseForm
from .models import Expense
from django.contrib import messages
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid registration details.")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            return render(request, 'login.html', {'error': 'Please fill in all fields'})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

# Dashboard (Show expenses)
@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'dashboard.html',  {'expenses': expenses})


@login_required
def monthly(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    monthly_totals = (
        expenses.values('date__year', 'date__month')
        .annotate(total=Sum('amount'))
        .order_by('date__year', 'date__month')  
    )
    return render(request, 'monthly.html',  {'monthly_totals': list(monthly_totals)})

# Add Expense
@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            if not expense.date: 
                from datetime import date
                expense.date = date.today()
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

# Edit Expense
@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense updated successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Failed to update expense.")
    else:
        form = ExpenseForm(instance=expense)
    
    return render(request, 'edit_expense.html', {'form': form, 'expense': expense})

# Delete Expense
@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    
    if request.method == 'POST':
        expense.delete()
        messages.success(request, "Expense deleted successfully!")
        return redirect('dashboard')
    
    return render(request, 'delete_expense.html', {'expense': expense})

def landing_page(request):
    
    return render(request, "landing.html")


