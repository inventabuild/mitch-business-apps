from django.db import models
from datetime import date
from company_manager import models as company_manager_models
from customer_manager import models as customer_manager_models
from customer_pricing_manager import models as customer_pricing_manager_models
from item_manager import models as item_manager_models

# Create your models here.
class Invoice(models.Model):
    company_id = models.ForeignKey(company_manager_models.Company, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(customer_manager_models.Customer, on_delete=models.CASCADE)
    item_id = models.ForeignKey(item_manager_models.Item, blank=True, null=True, on_delete=models.CASCADE)
    customer_pricing_id = models.ForeignKey(customer_pricing_manager_models.Customer_Pricing, blank=True, null=True, on_delete=models.CASCADE)    
    invoice_date = models.DateField(default=date.today)
    invoice_number = models.CharField(max_length=60, default='00000')
    po_num_row_1 = models.CharField(max_length=60, default='00000')
    po_num_row_2 = models.CharField(max_length=60, default='00000')
    po_num_row_3 = models.CharField(max_length=60, default='00000')
    po_num_row_4 = models.CharField(max_length=60, default='00000')
    po_num_row_5 = models.CharField(max_length=60, default='00000')
    item_num_row_1 = models.CharField(max_length=60, default='00000')
    item_num_row_2 = models.CharField(max_length=60, default='00000')
    item_num_row_3 = models.CharField(max_length=60, default='00000')
    item_num_row_4 = models.CharField(max_length=60, default='00000')
    item_num_row_5 = models.CharField(max_length=60, default='00000')
    item_name_row_1 = models.CharField(max_length=60, default='00000')
    item_name_row_2 = models.CharField(max_length=60, default='00000')
    item_name_row_3 = models.CharField(max_length=60, default='00000')
    item_name_row_4 = models.CharField(max_length=60, default='00000')
    item_name_row_5 = models.CharField(max_length=60, default='00000')
    customer_pricing_ea_row_1 = models.CharField(max_length=60, default='00000')
    customer_pricing_ea_row_2 = models.CharField(max_length=60, default='00000')
    customer_pricing_ea_row_3 = models.CharField(max_length=60, default='00000')
    customer_pricing_ea_row_4 = models.CharField(max_length=60, default='00000')
    customer_pricing_ea_row_5 = models.CharField(max_length=60, default='00000')
    qty_ea_row_1 = models.CharField(max_length=60, default='00000')
    qty_ea_row_2 = models.CharField(max_length=60, default='00000')
    qty_ea_row_3 = models.CharField(max_length=60, default='00000')
    qty_ea_row_4 = models.CharField(max_length=60, default='00000')
    qty_ea_row_5 = models.CharField(max_length=60, default='00000')
    amount_row_1 = models.CharField(max_length=60, default='00000')
    amount_row_2 = models.CharField(max_length=60, default='00000')
    amount_row_3 = models.CharField(max_length=60, default='00000')
    amount_row_4 = models.CharField(max_length=60, default='00000')
    amount_row_5 = models.CharField(max_length=60, default='00000')
    invoice_sales_amount = models.CharField(max_length=60, default='00000')
    invoice_freight_amount = models.CharField(max_length=60, default='00000')
    invoice_total_due = models.CharField(max_length=60, default='00000')
    invoice_age = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    invoice_paid = models.BooleanField(default=False)
    invoice_customer_check_number = models.CharField(max_length=60, default='00000')
    
    def _str_(self):
        return self.title