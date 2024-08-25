from django.db import models
from datetime import datetime
# Create your models here.
# Create your models here.
class Product(models.Model):
    X=[
        ('phone','phone'),
        ('laptop','laptop'),
        
    ]
    name = models.CharField(max_length=100)
    content = models.TextField(null= True,blank=True,verbose_name='Description')
    price =models.DecimalField(max_digits=6 ,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d',verbose_name='pHOTO')
    active= models.BooleanField(default=True)
    category=models.CharField(max_length=50,null= True ,blank= True , choices= X)
    
    def __str__(self):
        return self.name
    
    # class Meta:
    #     #verbose_name = 'model'
    #     ordering =['name']
        
class DateTest(models.Model):
    date = models.DateField()
    time = models.TimeField(null= True)
    both = models.DateTimeField(default= datetime.now)
    
    