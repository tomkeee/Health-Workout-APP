from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Value

# Create your models here.

class Profile (models.Model):
    account=models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"Account of {self.account}"

class Weight(models.Model):
    owner=models.ForeignKey(User,on_delete=CASCADE,null=True)
    value=models.FloatField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} - {} KG in {}".format(self.owner,self.value,self.date)
