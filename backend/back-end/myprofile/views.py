
from django.shortcuts import render
from django.http import JsonResponse as Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
    
from .serializers import user_profile_serializer
# Create your views here.
#from .models import User_Profile

from post.models import Post
from solutions.models import Solution

from users.models import CustomUser
from .models import User_Profile

from updateapi.models import User_Personal,User_Professional

from users.api.serializers import LoginSerializer
from updateapi.serializers import user_personal_serializer,user_professional_serializer
from post.serializers import PostSerializer
from solutions.serializers import SolutionSerializer
# Create your views here.

@api_view(['GET'])           #isauthenticated needed (sends back pswd)
def userProfileView(request,un):
	
	tasks = User_Profile.objects.filter(username=un)
	serializer = user_profile_serializer(tasks, many=True)
	
	#problem
	pos = Post.objects.filter(username=un)
	serializer2 =PostSerializer(pos, many=True)
	
	#solution
	sol = Solution.objects.filter(username=un)
	serializer3 = SolutionSerializer(sol, many=True)

	#user_personal
	personal = User_Personal.objects.filter(username=un)
	serializer4 = user_personal_serializer(personal,many = True)

	#user_professional
	professional = User_Professional.objects.filter(username=un)
	serializer5 = user_professional_serializer(professional,many = True)
	
	#email
	em = CustomUser.objects.filter(id=un)
	serializer6 = LoginSerializer(em, many=True)
	content={"email":serializer6.data[0].get('email')}
	
	Serializer_list = [serializer.data, serializer2.data,serializer3.data,serializer4.data,serializer5.data,content]
	
	return Response(Serializer_list,safe=False)  # returns list of json