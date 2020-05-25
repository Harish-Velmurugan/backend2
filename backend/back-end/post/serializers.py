from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        #fields = '__all__'
        fields=('username','problemId','title','description','RnD_Budget','deadline','skill','files','img')
  		

class PostSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'            