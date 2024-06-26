from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Record(models.Model):
    record_id = models.CharField(primary_key=True, max_length=9)
    creation_date = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    avatar = models.ImageField(default='avatar.png', blank=True)
    
    def __str__(self):
        return self.first_name

class Department(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'departments'

    def __str__(self):
        return self.name