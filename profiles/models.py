from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Value
import random

# Create your models here.

class Profile (models.Model):
    account=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    number=models.CharField(max_length=5,null=True,blank=True)

    def save(self,*args,**kwargs):
        number_list=[x for x in range(10)]
        code_items=[]

        for i in range(5):
            num=random.choice(number_list)
            code_items.append(num)
        
        code_string="".join(str(item) for item in code_items)
        self.number=code_string
        super().save(*args,**kwargs)
    

    def __str__(self):
        return f"Account of {self.account}"

class Weight(models.Model):
    owner=models.ForeignKey(User,on_delete=CASCADE,null=True)
    value=models.FloatField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} - {} KG in {}".format(self.owner,self.value,self.date)
