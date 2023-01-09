from .models import post
from rest_framework import viewsets, permissions
from .serializer import ParpadeoSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset=post.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ParpadeoSerializer