from datetime import datetime
from django.shortcuts import render
from customer_manager import models as customer_manager_models
from item_manager import models as item_manager_models
from . import models

# Create your views here.
def customer_pricing_view(request, id, wizStatus):
    customer_pricing_single=models.Customer_Pricing.objects.get(id=id)
    now = datetime.today().timestamp
    data={
        'customer_pricing_single': customer_pricing_single,
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'customer_pricing_manager/customer_pricing_view.html', data)
def customer_pricing_new(request, wizStatus):
    if request.method == "POST":
        try:
            customer_id=request.POST.get('customer_id')
            customer=customer_manager_models.Customer.objects.get(id=customer_id)
            item_id=request.POST.get('item_id')
            item=item_manager_models.Item.objects.get(id=item_id)
            new_customer_price = models.Customer_Pricing(
                customer_id=customer,
                item_id=item,
                # customer_id=request.POST.get('customer_id'),
                # item_id=request.POST.get('item_id'),
                customer_pricing=request.POST.get('customer_pricing')
            )
            new_customer_price.save()
            message = 'Customer pricing created'
        except:
            message = "Error creating customer pricing"
    else:
        message = ''
    customers_all=customer_manager_models.Customer.objects.all().order_by('name')
    items_all=item_manager_models.Item.objects.all().order_by('name')
    now = datetime.today().timestamp
    data = {
        'customers_all': customers_all,
        'items_all': items_all,
        'message': message,
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'customer_pricing_manager/customer_pricing_new.html', data)

def customer_pricing_list(request, wizStatus):
    customer_pricing_all=models.Customer_Pricing.objects.all().order_by('-id')
    now = datetime.today().timestamp
    data = {
        'customer_pricing_all': customer_pricing_all,
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'customer_pricing_manager/customer_pricing_list.html', data)
def customer_pricing_options_list(request, wizStatus):
    now = datetime.today().timestamp
    data = {
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'customer_pricing_manager/customer_pricing_options_list.html', data)
