from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from .models import Task

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<int:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<int:pk>/',
        'Delete': '/task-delete/<int:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def TaskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializers = TaskSerializer(tasks, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def TaskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializers = TaskSerializer(tasks, many=False)
    return Response(serializers.data)


@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def TaskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def TaskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item Deleted Successfully')
