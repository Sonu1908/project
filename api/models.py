from django.db import models

# Create your models here.

#Creating Dataviv Invoice



class Invoice(models.Model):
    invoice_id= models.AutoField(primary_key=True)
    date= models.DateField(auto_now_add=True)
    customer = models.TextField(default='')
    contact= models.CharField(max_length=255, default='', blank=True, null=True)
    location= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    comments= models.TextField(default='',blank=True,null=True)
    total= models.FloatField(default=0)
    active=models.BooleanField(default=True)



    def __str__(self):
        return self.name +self.location




 

