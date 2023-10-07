from django.db import models

# Create your models here.
class emod(models.Model):
    s_no = models.IntegerField()
    date=models.DateField()
    Total_amount = models.CharField(max_length=246,null=True,default=0)
    amt=models.CharField(max_length=246)
    expense = models.CharField(max_length=246)
    amt_taken =models.CharField(max_length=246)
    


