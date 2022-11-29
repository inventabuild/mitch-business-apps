from datetime import datetime
from django.shortcuts import render
from . import models

# Create your views here.
def item_new(request):
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
        'now': now
    }
    return render(request, 'item_manager/item_new.html', data)
def item_view(request, id):
    item_single=models.Item.objects.get(id=id)
    data={
        'item_single': item_single
    }
    return render(request, 'item_manager/item_view.html', data)

def item_list(request):
    list_all=models.Item.objects.all().order_by('name')
    now = datetime.today().timestamp
    data={
        'list_all': list_all,
        'now': now
    }
    return render(request, 'item_manager/item_list.html', data)
def item_options_list(request):
    return render(request, 'item_manager/item_options_list.html')