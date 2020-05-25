from django.db import models
from post.models import Post
from users.models import CustomUser

class Solution(models.Model):

    username = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE) # id of particular team (user id can be fetched)
    problemId = models.ForeignKey(to= Post , on_delete= models.CASCADE,db_column='problemId') # id of particular problem
    solutionId = models.AutoField(primary_key=True) # generated id for solution to be submitted
    
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100) 
    abstract = models.CharField(max_length=500) 
    docs = models.FileField(upload_to='documents')
    image = models.ImageField(upload_to= 'solution_images',null=True) # uploading image files
    video = models.FileField(upload_to='videos',null=True) # uploading video file
    soln_date = models.DateTimeField(auto_now_add=True)
    status= models.BooleanField(default = False)
    level= models.CharField(max_length=50, default='unsolved')
    votes= models.IntegerField(default=0) 

    def __str__(self):
        return self.title