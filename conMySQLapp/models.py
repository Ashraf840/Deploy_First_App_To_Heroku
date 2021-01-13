from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Student Name', max_length=200)
    roll = models.PositiveIntegerField(verbose_name='Roll no.')
    phone = models.CharField(verbose_name='Contact', max_length=14)
    email = models.EmailField(verbose_name='Email Address', max_length=60, unique=True, blank=True, null=True)
