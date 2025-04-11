from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import FinanceRecord, Loan

def index(request):
    return render(request, "index.html")
def emi(request):
    return render(request, "tools/emi.html")
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print("hi")
        if user is not None:
            login(request, user)
            return redirect("dashboard") 
        else:
            return render(request, "auth/login.html", {"error": "Invalid credentials"})

    return render(request, "auth/login.html")

@login_required
def dashboard_view(request):
    if request.method == "POST":
        date = request.POST.get("date")
        category = request.POST.get("category")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        types = request.POST.get("types")

        if date and category and amount:
            FinanceRecord.objects.create(
                user=request.user,
                date=date,
                category=category,
                amount=amount,
                name=description,
                type=types
            )

        finance_data = FinanceRecord.objects.filter(user=request.user).order_by('-date')

        return render(request, 'user/home.html', {'finance_data': finance_data})

    finance_data = FinanceRecord.objects.filter(user=request.user).order_by('-date')

    return render(request, 'user/home.html', {'finance_data': finance_data})

@login_required
def loan_view(request):
    if request.method == "POST":
        date = request.POST.get("date")
        category = request.POST.get("category")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        types = request.POST.get("types")

        if date and category and amount:
            FinanceRecord.objects.create(
                user=request.user,
                date=date,
                category=category,
                amount=amount,
                name=description,
                type=types
            )

        finance_data = FinanceRecord.objects.filter(user=request.user).order_by('-date')

        return render(request, 'user/home.html', {'finance_data': finance_data})

    finance_data = FinanceRecord.objects.filter(user=request.user).order_by('-date')

    return render(request, 'user/home.html', {'finance_data': finance_data})

def logout_view(request):
    logout(request)
    return redirect('login')
