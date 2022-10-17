from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=60)
    address=models.CharField(max_length=60)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=60)
    country=models.CharField(max_length=60)
    zip_code=models.CharField(max_length=10)
    
    def _str_(self):
        return self.title