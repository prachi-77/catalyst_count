from enum import unique
from django.db import models

# Create your models here.
class CompanyData(models.Model):
    class Meta:
        
        db_table = 'company_data'
    id= models.IntegerField(primary_key=True)
    count = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    domain = models.CharField(max_length=256)
    year_founded=models.CharField(max_length=256)
    industry=models.CharField(max_length=256)
    size_range=models.CharField(max_length=256)
    # locality=models.TextField()
    country=models.CharField(max_length=256)
    linkedin_url=models.TextField()
    current_employee_estimate=models.CharField(max_length=256)
    total_employee_estimate=models.CharField(max_length=256)
    city=models.CharField(max_length=256)
    state=models.CharField(max_length=256)
    
