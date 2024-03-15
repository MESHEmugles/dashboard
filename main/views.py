from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.views.generic import View

from .models import *
from .serializers import *

# Create your views here.

class Home(APIView):
    
    def get(self, request):
        return render(request, 'main/index.html')

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDelete(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectUpdate(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend ]
    search_fields =['proj__name', 'name', 'text']
    def get_queryset(self):
        queryset = super().get_queryset()
        proj_status = self.request.query_params.get('proj_status')
        if proj_status:
            queryset = queryset.filter(proj__status=proj_status)
        return queryset

    # try:
    #     filter_backends = [DjangoFilterBackend, filters.SearchFilter ]
    #     filterset_fields = ['proj__status']
    # except:
    #     filter_backends = [filters.SearchFilter]
    #     search_fields =['proj__name', 'name', 'text']

class TaskUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer





