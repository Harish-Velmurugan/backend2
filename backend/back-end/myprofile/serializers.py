from rest_framework import serializers
from .models import User_Profile
class user_profile_serializer(serializers.ModelSerializer):

    class Meta:
        model = User_Profile
        fields ='__all__'