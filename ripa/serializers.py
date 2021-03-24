from rest_framework import serializers
from .models import Issue

class IssueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Issue
        fields = ("title", "description")
