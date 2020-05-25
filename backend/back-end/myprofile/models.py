from django.db import models

from django.db.models import IntegerField, Model
from django_mysql.models import ListTextField

from users.models import CustomUser

class User_Profile(models.Model):
    
    username = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, primary_key=True)

    problems_interested= ListTextField(
        base_field=IntegerField()
    )