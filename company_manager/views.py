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
    data = {
        'message': message
    }
    return render(request, 'company_manager/company_new.html', data)