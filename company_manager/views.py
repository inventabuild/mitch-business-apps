from datetime import datetime
from django.shortcuts import render
from . import models

# Create your views here.
def company_options_list(request):
    return render(request, 'company_manager/company_options_list.html')
def company_new(request):
    if request.method == "POST":
        try:
            new_company = models.Company(
                name=request.POST.get('company_name'),
                address=request.POST.get('company_address'),
                city=request.POST.get('company_city'),
                state=request.POST.get('company_state'),
                country=request.POST.get('company_country'),
                zip_code=request.POST.get('company_zip_code'),
                tel=request.POST.get('company_tel'),
            )
            new_company.save()
            message = 'Company successfully created'
        except:
            message = 'New company failed'
    else:
        message = ''
    now = datetime.today().timestamp
    data = {
        'message': message,
        'now': now
    }
    return render(request, 'company_manager/company_new.html', data)
def company_view(request, id):
    company_single=models.Company.objects.get(id=id)
    data={
        'company_single': company_single
    } 
    return render(request, 'company_manager/company_view.html', data)
def company_list(request):
    company_all=models.Company.objects.all().order_by('name')
    now = datetime.today().timestamp
    data = {
        'company_all': company_all,
        'now': now
    }
    return render(request, 'company_manager/company_list.html', data)