from rest_framework import serializers
from .models import Solution

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('username', 'solutionId','problemId','title', 'desc', 'abstract', 'docs' , 'image', 'video', 'soln_date')


class SolutionSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'        