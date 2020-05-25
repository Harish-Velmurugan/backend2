from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse as Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
    
from solutions.serializers import SolutionSerializer, SolutionSerializer2

from post.models import Post 
from solutions.models import Solution 

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def solutionSubmissionView(request):
   pid = request.POST.get("problemId")
   serializer = SolutionSerializer(data=request.data)
   if serializer.is_valid():
         serializer.save()
         c=(serializer.data["problemId"])
         d=Post.objects.get(problemId=c)
         d.sol_count+=1
         d.save()
   return Response(serializer.data)
   
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def voteView(request,pk):
      task = Solution.objects.get(solutionId=pk) 
      print(task.votes)
      task.votes+=1
      task.save()
      return Response({"values":"success"}) 
