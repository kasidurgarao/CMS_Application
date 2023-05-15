from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import generics, permissions
from .models import customer, Post, Like
from .serializers import customerSerializer, PostSerializer, LikeSerializer


class home(View):
    def get(self, request, *args, **kwargs):
        return render(request, "cms_application/base.html")

class customerListCreateView(generics.ListCreateAPIView):
    queryset = customer.objects.all()
    serializer_class = customerSerializer


class customerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = customer.objects.all()
    serializer_class = customerSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['request'] = self.request
    #     return context
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.annotate(like_count=models.Count('like_count'))
    #     return queryset

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

