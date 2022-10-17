from django.shortcuts import render
from . import models

# Create your views here.
def customer_new(request):
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
    data = {
        'message': message
    }
    return render(request, 'customer_manager/customer_new.html', data)
def customer_view(request, id):
    customer_single=models.Customer.objects.get(id=id)
    data={
        'customer_single': customer_single
    } 
    return render(request, 'customer_manager/customer_view.html', data)
def customer_list(request):
    customers_all=models.Customer.objects.all().order_by('name')
    data = {
        'customers_all': customers_all
    }
    return render(request, 'customer_manager/customer_list.html', data)
def customer_options_list(request):
    return render(request, 'customer_manager/customer_options_list.html')