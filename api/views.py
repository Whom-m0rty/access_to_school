from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Post
from .serializers import PostSerializer
# Create your views here.

class PostView(APIView):
    def get(request, self, slug):
        post = Post.objects.get(slug__iexact=slug)
        serializer = PostSerializer(post)
        return Response({'post': serializer.data})
