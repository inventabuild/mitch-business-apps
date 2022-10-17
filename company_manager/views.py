from django.shortcuts import render

# Create your views here.
def company_options_list(request):
    return render(request, 'company_manager/company_options_list.html')