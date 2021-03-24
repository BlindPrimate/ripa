# from django.shortcuts import render
from rest_framework import viewsets
from .models import Issue
from .serializers import IssueSerializer

# Create your views here.
class IssueView(viewsets.ModelViewSet):
    queryset = Issue.objects.all().order_by("title")
    serializer_class = IssueSerializer
