from django.db import models

class Datas(models.Model):
    Fullname=models.CharField(max_length=25,default="")
    Email=models.CharField(max_length=35,default="")
    Message=models.CharField(max_length=50,default="")

# Create your models here.
