from django.db import models

# Create your models here.
class Item(models.Model):
    number=models.CharField(max_length=60)
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=60)
    item_cost_internal=models.CharField(max_length=60)
    
    def _str_(self):
        return self.title