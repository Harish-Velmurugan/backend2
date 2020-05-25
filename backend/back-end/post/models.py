from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from unittest.util import _MAX_LENGTH
from getpass import getuser
from datetime import datetime, timedelta
from multiselectfield import MultiSelectField
from django_mysql.models import ListCharField
from django.db.models import CharField, Model
from users.models import CustomUser 

class Post(models.Model):

    username = models.ForeignKey(to=CustomUser,on_delete=models.CASCADE,db_column='username')
    problemId = models.AutoField(primary_key=True)#unique id for each problem    
    title = models.CharField(max_length=50)
    description = models.TextField()
    RnD_Budget=models.CharField(max_length=20) 
    posteddate = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=datetime.now())
    # skill=MultiSelectField(max_length=20, choices=SKILLS)
    # skill=models.CharField(choices=SKILLS,max_length=20)
    skill=ListCharField(
        base_field=CharField(max_length=20),
        size=5,
        max_length=(5 * 21))
    files=models.FileField(upload_to='file')
    img=models.ImageField(upload_to='problem_images')
    sol_count=models.IntegerField(default = 0)
    
    def __str__(self):
        return self.title
