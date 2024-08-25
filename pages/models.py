from django.db import models


#one to one rel
class Female(models.Model):
    female_name = models.CharField(max_length=100)
    def __str__(self):
        return self.female_name
            
class Male(models.Model):
    male_name = models.CharField(max_length=100)
    girls = models.OneToOneField(Female,on_delete=models.CASCADE)
    def  __str__(self):
        return self.male_name
    
#one to many rell
class Product(models.Model):
    title =  models.CharField(max_length=100 )
    def __str__(self) :
        return self.title
    
class User(models.Model):
    name = models.CharField(max_length=100 )
    products = models.ForeignKey(Product, on_delete= models.PROTECT)
    def __str__(self):
        return self.name

#many to many
class Book(models.Model):
    book = models.CharField(max_length=100 ,null= True)
    def  __str__(self):
        return self.book
    
class Reader(models.Model):
    reader = models.CharField(max_length=100,null= True)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.reader


