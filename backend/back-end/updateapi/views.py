from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import user_personal_serializer,user_professional_serializer,bids_serializer
# Create your views here.
from .models import User_Personal,User_Professional,bids

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userProfessionalGetView(request, pk):
    user  = User_Professional.objects.get(username=pk)
    serializer = user_professional_serializer(instance=user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userPersonalGetView(request, pk):
    user  = User_Personal.objects.get(username=pk)
    serializer = user_personal_serializer(instance=user)
    return Response(serializer.data)

@api_view(['GET'])
def userPersonalView(request):
	tasks = User_Personal.objects.all().order_by('-id')
	serializer = user_personal_serializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def userProfessionalView(request):
	tasks = User_Professional.objects.all()
	serializer = user_professional_serializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userPersonalCreateView(request):
    serializer = user_personal_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userProfessionalCreateView(request):
    serializer = user_professional_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userPersonalUpdateView(request, pk):
    user  = User_Personal.objects.get(username=pk)
    serializer = user_personal_serializer(instance=user,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userProfessionalUpdateView(request, pk):
    user  = User_Professional.objects.get(username=pk)
    serializer = user_professional_serializer(instance=user,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)