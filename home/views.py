from datetime import datetime
from django.shortcuts import render
from django.core import serializers

# Create your views here.
def index(request, wizStatus):
    now = datetime.today().timestamp
    x=10
    data={
        'now':now,
        'x':x,
        'wizStatus': wizStatus
    }
    return render(request, 'home/index.html', data)