from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models



class Infor(models.Model):

    name = models.CharField(max_length=100)
    student_id  = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    objections = models.CharField(max_length=100,null=True)
