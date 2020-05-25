
from updateapi.models import User_Personal
from updateapi.serializers import user_personal_serializer
from solutions.models import Solution
from solutions.serializers import SolutionSerializer
from post.models import Post
from post.serializers import PostSerializer
from rest_framework import generics,filters
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet,FlatMultipleModelAPIViewSet

class SearchAPIView(ObjectMultipleModelAPIViewSet):

    def get_querylist(self):
        search_query=self.request.query_params['q']
    
        querylist = (

             {'queryset': User_Personal.objects.filter(firstname__icontains=search_query), 'serializer_class':user_personal_serializer},
             {'queryset': Post.objects.filter(title__icontains=search_query) , 'serializer_class': PostSerializer},
             {'queryset': Solution.objects.filter(title__icontains=search_query),'serializer_class': SolutionSerializer},
        )
        return querylist
