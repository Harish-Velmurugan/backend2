from rest_framework import serializers
from .models import User_Professional,User_Personal,bids

class user_professional_serializer(serializers.ModelSerializer):

    class Meta:
        model = User_Professional
        fields = '__all__'

class user_personal_serializer(serializers.ModelSerializer):

    class Meta:
        model = User_Personal
        fields = '__all__'

class bids_serializer(serializers.ModelSerializer):

    class Meta:
        model = bids
        fields = '__all__'