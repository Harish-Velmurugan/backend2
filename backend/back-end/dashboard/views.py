from django.shortcuts import render
from django.http import JsonResponse as response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
    
from post.serializers import PostSerializer2
# Create your views here.
from post.models import Post
from solutions.models import Solution

from solutions.serializers import SolutionSerializer2

from updateapi.serializers import user_personal_serializer,user_professional_serializer
# Create your views here.
from updateapi.models import User_Personal,User_Professional

'''# Create your views here.
@api_view(['GET'])
def problemInvolvedView(request,pk):
    tasks = Post.objects.all().order_by('-id')	
   	serializer = user_personal_serializer(tasks, many=True)
	return response(serializer.data)
'''
@api_view(['GET'])
def dashboardPPView(request,pk):
    tasks  = Post.objects.filter(username=pk)
    serializer = PostSerializer2(tasks,many=True)
    return response(serializer.data,safe=False)

@api_view(['GET'])
def postedProblemView(request,pk):
    tasks = Solution.objects.filter(problemId=pk)
    serializer = SolutionSerializer2(tasks, many=True)
    return response(serializer.data,safe=False)

