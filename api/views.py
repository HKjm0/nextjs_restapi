# from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer, PostSerializer
from .models import Task, Post


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)  # JWTで認証される前なのでAllowAnyにしておく


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


# ModelViewSetを継承してきた場合はCRUD　Create（生成）、Read（読み取り）、Update（更新）、Delete 、(削除）が全て利用できる
class TaskViewSet(viewsets.ModelViewSet):
    queryset: object = Task.objects.all()
    serializer_class = TaskSerializer
