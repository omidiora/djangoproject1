from django.shortcuts import render,redirect
from .models import *
from .forms import CustomerForm
# Create your views here.

def home(request):
    customer=Customer.objects.all()
    total_customers=customer.count()
    order=Order.objects.all()
    pending=order.filter(status="pending").count()
    delivered=order.filter(status='Delivered').count()
    context={'total_customers':total_customers,'orders':order,'pending':pending,'delivered':delivered}
    return render(request,'index.html',context)

def accountsetting(request):
    form=CustomerForm(request.POST)
    if request.method=='POST':
            form=CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                context={'form':form}
                return redirect('/')
    context={'form':form}
    return render(request,'account.html',context)