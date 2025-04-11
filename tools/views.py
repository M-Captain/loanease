from django.shortcuts import render

# Create your views here.
def emiCalculator(request):
    return render(request,"tools/emi.html")