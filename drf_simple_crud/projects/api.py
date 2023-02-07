from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """What queries can be done"""
    queryset = Project.objects.all()    
    permission_classes = [permissions.AllowAny] #allow any client to make queries to the app
    serializer_class = ProjectSerializer
