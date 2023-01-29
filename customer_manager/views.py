from datetime import datetime
from django.shortcuts import render
from . import models

# Create your views here.
def customer_new(request, wizStatus):
    if request.method == "POST":
        try:
            new_customer = models.Customer(
                name=request.POST.get('customer_name'),
                address=request.POST.get('customer_address'),
                city=request.POST.get('customer_city'),
                state=request.POST.get('customer_state'),
                country=request.POST.get('customer_country'),
                zip_code=request.POST.get('customer_zip_code')
            )
            new_customer.save()
            message = 'Customer created'
        except:
            message = "Error creating the customer"
    else:
        message = ''
    now = datetime.today().timestamp
    data = {
        'message': message,
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'customer_manager/customer_new.html', data)
def customer_view(request, id, wizStatus):
    customer_single=models.Customer.objects.get(id=id)
    now = datetime.today().timestamp
    data={
        'customer_single': customer_single,
        'now': now,
        'wizStatus': wizStatus
    } 
    return render(request, 'customer_manager/customer_view.html', data)
def customer_list(request, wizStatus):
    customers_all=models.Customer.objects.all().order_by('-id')
    now = datetime.today().timestamp
    data = {
        'customers_all': customers_all,
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'customer_manager/customer_list.html', data)
def customer_options_list(request, wizStatus):
    now = datetime.today().timestamp
    data = {
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'customer_manager/customer_options_list.html', data)