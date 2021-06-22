from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
    

class Sweetshop(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
    address=models.CharField(max_length= 200,null = True,blank=True)
    map_link=models.CharField(max_length=500,null=True,blank=True)
    rating=models.IntegerField( default=0,validators=[MaxValueValidator(5), MinValueValidator(0)])
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")]  ,max_length=20, null = True)
    email= models.EmailField(unique=True,null=True,blank=True)
    review = models.TextField(null= True,blank=True) 
    image=models.ImageField(upload_to = "images//", null=True,blank=True)
    menu=models.ImageField(upload_to = "images//", null=True, blank=True)
    
    pic1=models.ImageField(upload_to = "images//", null=True,blank=True)
    pic2=models.ImageField(upload_to = "images//", null=True,blank=True)
    pic3=models.ImageField(upload_to = "images//", null=True,blank=True)
    pic4=models.ImageField(upload_to = "images//", null=True,blank=True)
    pic5=models.ImageField(upload_to = "images//", null=True,blank=True)
    pic6=models.ImageField(upload_to = "images//", null=True,blank=True)
    
