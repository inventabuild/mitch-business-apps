from datetime import datetime
from django.shortcuts import render
from . import models
from company_manager import models as company_manager_models
from customer_manager import models as customer_manager_models
from customer_pricing_manager import models as customer_pricing_manager_models
from item_manager import models as item_manager_models
from django.core import serializers
from django.contrib import messages

# Create your views here.
def invoice_view(request, id, wizStatus):
    invoice_single = models.Invoice.objects.get(id=id)
    now = datetime.today().timestamp
    data = {
        'invoice_single': invoice_single,
        'now': now,
        'wizStatus': wizStatus
        }
    return render(request, 'invoice_manager/invoice_view.html', data)
def invoice_list(request, wizStatus):
    invoice_all = models.Invoice.objects.all().order_by('-id')
    now = datetime.today().timestamp
    data = {
        'invoice_all': invoice_all,
        'now': now,
        'wizStatus': wizStatus
        }
    return render(request, 'invoice_manager/invoice_list.html', data)
def invoice_options_list(request, wizStatus):
    now = datetime.today().timestamp
    data={
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'invoice_manager/invoice_options_list.html', data)
def invoice_new_view_edit(request, id, wizStatus):
    if request.method == 'POST':
        try:
            company_id = request.POST.get('company-select')
            company = company_manager_models.Company.objects.get(id=company_id)
            customer_id = request.POST.get('customer-select')
            customer = customer_manager_models.Customer.objects.get(id=customer_id)
            item_id_row_1 = request.POST.get('item-num-select-1')
            if (item_id_row_1 != '-1' and item_id_row_1 != '-2'):
                item_id_row_1_object = item_manager_models.Item.objects.get(id=item_id_row_1)
                item_num_row_1 = item_id_row_1_object.number
                item_name_row_1 = item_id_row_1_object.name
            else:
                item_num_row_1 = ''
                item_name_row_1 = ''
            item_id_row_2 = request.POST.get('item-num-select-2')
            if (item_id_row_2 != '-1' and item_id_row_2 != '-2'):
                item_id_row_2_object = item_manager_models.Item.objects.get(id=item_id_row_2)
                item_num_row_2 = item_id_row_2_object.number
                item_name_row_2 = item_id_row_2_object.name
            else:
                item_num_row_2 = ''
                item_name_row_2 = ''
            item_id_row_3 = request.POST.get('item-num-select-3')
            if (item_id_row_3 != '-1' and item_id_row_3 != '-2'):
                item_id_row_3_object = item_manager_models.Item.objects.get(id=item_id_row_3)
                item_num_row_3 = item_id_row_3_object.number
                item_name_row_3 = item_id_row_3_object.name
            else:
                item_num_row_3 = ''
                item_name_row_3 = ''
            item_id_row_4 = request.POST.get('item-num-select-4')
            if (item_id_row_4 != '-1' and item_id_row_4 != '-2'):
                item_id_row_4_object = item_manager_models.Item.objects.get(id=item_id_row_4)
                item_num_row_4 = item_id_row_4_object.number
                item_name_row_4 = item_id_row_4_object.name
            else:
                item_num_row_4 = ''
                item_name_row_4 = ''
            item_id_row_5 = request.POST.get('item-num-select-5')
            if (item_id_row_5 != '-1' and item_id_row_5 != '-2'):
                item_id_row_5_object = item_manager_models.Item.objects.get(id=item_id_row_5)
                item_num_row_5 = item_id_row_5_object.number
                item_name_row_5 = item_id_row_5_object.name
            else:
                item_num_row_5 = ''
                item_name_row_5 = ''
            price_ea_row_1 = request.POST.get('price-ea-input-1')
            if(price_ea_row_1 == "--Read only--"):
                price_ea_row_1 = ''
            price_ea_row_2 = request.POST.get('price-ea-input-2')
            if(price_ea_row_2 == "--Read only--"):
                price_ea_row_2 = ''
            price_ea_row_3 = request.POST.get('price-ea-input-3')
            if(price_ea_row_3 == "--Read only--"):
                price_ea_row_3 = ''
            price_ea_row_4 = request.POST.get('price-ea-input-4')
            if(price_ea_row_4 == "--Read only--"):
                price_ea_row_4 = ''
            price_ea_row_5 = request.POST.get('price-ea-input-4')
            if(price_ea_row_5 == "--Read only--"):
                price_ea_row_5 = ''
            amount_row_1 = request.POST.get('amount-dollar-input-1')
            if(amount_row_1 == "--Read only--"):
                amount_row_1 = ''
            amount_row_2 = request.POST.get('amount-dollar-input-2')
            if(amount_row_2 == "--Read only--"):
                amount_row_2 = ''
            amount_row_3 = request.POST.get('amount-dollar-input-3')
            if(amount_row_3 == "--Read only--"):
                amount_row_3 = ''
            amount_row_4 = request.POST.get('amount-dollar-input-4')
            if(amount_row_4 == "--Read only--"):
                amount_row_4 = ''
            amount_row_5 = request.POST.get('amount-dollar-input-5')
            if(amount_row_5 == "--Read only--"):
                amount_row_5 = ''
            if(id == 1):
                new_invoice = models.Invoice(
                    company_id = company,
                    customer_id = customer,
                    invoice_number = request.POST.get('invoice-number'),
                    invoice_date = request.POST.get('invoice-date'),
                    po_num_row_1 = request.POST.get('po-num-input-1'),
                    po_num_row_2 = request.POST.get('po-num-input-2'),
                    po_num_row_3 = request.POST.get('po-num-input-3'),
                    po_num_row_4 = request.POST.get('po-num-input-4'),
                    po_num_row_5 = request.POST.get('po-num-input-5'),
                    item_num_row_1 = item_num_row_1,
                    item_name_row_1 = item_name_row_1,
                    item_num_row_2 = item_num_row_2,
                    item_name_row_2 = item_name_row_2,
                    item_num_row_3 = item_num_row_3,
                    item_name_row_3 = item_name_row_3,
                    item_num_row_4 = item_num_row_4,
                    item_name_row_4 = item_name_row_4,
                    item_num_row_5 = item_num_row_5,
                    item_name_row_5 = item_name_row_5,
                    customer_pricing_ea_row_1 = price_ea_row_1,
                    customer_pricing_ea_row_2 = price_ea_row_2,
                    customer_pricing_ea_row_3 = price_ea_row_3,
                    customer_pricing_ea_row_4 = price_ea_row_4,
                    customer_pricing_ea_row_5 = price_ea_row_5,
                    qty_ea_row_1 = request.POST.get('qty-ea-input-1'),
                    qty_ea_row_2 = request.POST.get('qty-ea-input-2'),
                    qty_ea_row_3 = request.POST.get('qty-ea-input-3'),
                    qty_ea_row_4 = request.POST.get('qty-ea-input-4'),
                    qty_ea_row_5 = request.POST.get('qty-ea-input-5'),
                    amount_row_1 = amount_row_1,
                    amount_row_2 = amount_row_2,
                    amount_row_3 = amount_row_3,
                    amount_row_4 = amount_row_4,
                    amount_row_5 = amount_row_5,
                    invoice_sales_amount = request.POST.get('sales-amount-input'),
                    invoice_freight_amount = request.POST.get('freight-amount-input'),
                    invoice_total_due = request.POST.get('invoice-total')
                )
                new_invoice.save()
            else:
                update_invoice = models.Invoice(
                    id = id,
                    company_id = company,
                    customer_id = customer,
                    invoice_number = request.POST.get('invoice-number'),
                    invoice_date = request.POST.get('invoice-date'),
                    po_num_row_1 = request.POST.get('po-num-input-1'),
                    po_num_row_2 = request.POST.get('po-num-input-2'),
                    po_num_row_3 = request.POST.get('po-num-input-3'),
                    po_num_row_4 = request.POST.get('po-num-input-4'),
                    po_num_row_5 = request.POST.get('po-num-input-5'),
                    item_num_row_1 = item_num_row_1,
                    item_name_row_1 = item_name_row_1,
                    item_num_row_2 = item_num_row_2,
                    item_name_row_2 = item_name_row_2,
                    item_num_row_3 = item_num_row_3,
                    item_name_row_3 = item_name_row_3,
                    item_num_row_4 = item_num_row_4,
                    item_name_row_4 = item_name_row_4,
                    item_num_row_5 = item_num_row_5,
                    item_name_row_5 = item_name_row_5,
                    customer_pricing_ea_row_1 = price_ea_row_1,
                    customer_pricing_ea_row_2 = price_ea_row_2,
                    customer_pricing_ea_row_3 = price_ea_row_3,
                    customer_pricing_ea_row_4 = price_ea_row_4,
                    customer_pricing_ea_row_5 = price_ea_row_5,
                    qty_ea_row_1 = request.POST.get('qty-ea-input-1'),
                    qty_ea_row_2 = request.POST.get('qty-ea-input-2'),
                    qty_ea_row_3 = request.POST.get('qty-ea-input-3'),
                    qty_ea_row_4 = request.POST.get('qty-ea-input-4'),
                    qty_ea_row_5 = request.POST.get('qty-ea-input-5'),
                    amount_row_1 = amount_row_1,
                    amount_row_2 = amount_row_2,
                    amount_row_3 = amount_row_3,
                    amount_row_4 = amount_row_4,
                    amount_row_5 = amount_row_5,
                    invoice_sales_amount = request.POST.get('sales-amount-input'),
                    invoice_freight_amount = request.POST.get('freight-amount-input'),
                    invoice_total_due = request.POST.get('invoice-total')
                )
                update_invoice.save()
            message="Invoice created successfully"
        except:
            message="There was an error saving the invoice"
    else:
        message=""
    invoice_single = models.Invoice.objects.get(id=id)
    json_invoice_single = serializers.serialize('json', models.Invoice.objects.filter(id=id))
    invoice_all = models.Invoice.objects.all().order_by('id')
    json_invoice_all = serializers.serialize('json', models.Invoice.objects.all().order_by('id'))
    company_all = company_manager_models.Company.objects.all().order_by('name')
    json_company_all = serializers.serialize('json', company_manager_models.Company.objects.all().order_by('name'))
    customer_all = customer_manager_models.Customer.objects.all().order_by('name')
    json_customer_all = serializers.serialize('json', customer_manager_models.Customer.objects.all().order_by('name'))
    customer_pricing_all = customer_pricing_manager_models.Customer_Pricing.objects.all().order_by('customer_id')
    json_customer_pricing_all = serializers.serialize('json', customer_pricing_manager_models.Customer_Pricing.objects.all().order_by('item_id'))
    item_all = item_manager_models.Item.objects.all().order_by('name')
    json_item_all = serializers.serialize('json', item_manager_models.Item.objects.all().order_by('name'))
    now = datetime.today().timestamp
    data = {
        'invoice_single': invoice_single,
        'invoice_all': invoice_all,
        'json_invoice_all': json_invoice_all,
        'company_all': company_all,
        'customer_all': customer_all,
        'customer_pricing_all': customer_pricing_all,
        'item_all': item_all,
        'message': message,
        'json_invoice_single': json_invoice_single,
        'json_company_all': json_company_all,
        'json_customer_all': json_customer_all,
        'json_item_all': json_item_all,
        'json_customer_pricing_all': json_customer_pricing_all,
        'now': now,
        'wizStatus': wizStatus
        }
    return render(request, 'invoice_manager/invoice_new_view_edit.html', data)