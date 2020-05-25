from django.shortcuts import render
from rest_framework import viewsets 
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes

#from updateapi.models import User_Profile

# @permission_classes([IsAuthenticated])
class PostView(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
'''
@api_view(['POST'])
def bookmarks (request, un, pid):
    task = User_Profile.objects.filter(username = un)
    task.problems_interested.append(pid)
    task.save()
    print(task)

'''
# @api_view(['POST'])
# # @permission_classes([IsAuthenticated])
# def voteView(request,pk):
#       task = Solution.objects.get(solutionId=pk)
#       print(task.votes)
#       task.votes+=1
#       task.save()
#       return Response({"values":"success"})
