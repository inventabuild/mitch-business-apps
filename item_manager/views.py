from datetime import datetime
from django.shortcuts import render
from . import models

# Create your views here.
def item_options_list_wizard(request, wizStatus):
    now = datetime.today().timestamp
    data = {
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'item_manager/item_options_list.html', data)
def item_new_wizard(request, wizStatus):
    if request.method == "POST":
        try:
            new_item = models.Item(
                number=request.POST.get('item_number'),
                name=request.POST.get('item_name'),
                description=request.POST.get('item_description'),
                item_cost_internal=request.POST.get('item_cost_internal')
            )
            new_item.save()
            message='Item created successfully'
        except:
            message='Error saving the item'
    else:
        message=''
    now = datetime.today().timestamp
    data = {
        'message': message,
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'item_manager/item_new.html', data)
def item_view_wizard(request, id, wizStatus):
    item_single=models.Item.objects.get(id=id)
    now = datetime.today().timestamp
    data={
        'item_single': item_single,
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'item_manager/item_view.html', data)
def item_list_wizard(request, wizStatus):
    list_all=models.Item.objects.all().order_by('-id', )
    now = datetime.today().timestamp
    data={
        'list_all': list_all,
        'now': now,
        'wizStatus': wizStatus
    }
    return render(request, 'item_manager/item_list.html', data)