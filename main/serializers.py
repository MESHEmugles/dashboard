from datetime import datetime, timedelta

from django.db.models import fields
from rest_framework import serializers
from .models import *


class CustomTimeField(serializers.Field):
    def to_representation(self, value):
        if not value:
            return None

        now = datetime.utcnow().replace(tzinfo=value.tzinfo)
        diff = now - value

        if diff.days > 0:
            return f"{diff.days}d"
        elif diff.seconds >= 3600:
            return f"{diff.seconds // 3600}h"
        elif diff.seconds >= 60:
            return f"{diff.seconds // 60}m"
        else:
            return f"{diff.seconds}s"


class TaskSerializer(serializers.ModelSerializer):
    # author_name = serializers.ReadOnlyField(source = 'author.name')
    proj_name = serializers.ReadOnlyField(source = 'proj.name')
    proj_status = serializers.ReadOnlyField(source = 'proj.status')
    created = serializers.DateTimeField(format="%b %d, %Y", read_only=True)
    readabletime = CustomTimeField(source='due_date')

    class Meta:
        model = Task
        fields = ['id', 'name', 'slug', 'due_date', 'priority', 'iscompleted', 'created', 'updated', 'status','img','readabletime', 'proj_name', 'proj','proj_status', 'text']


class ProjectSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many= True, required = False)
    created = serializers.DateTimeField(format="%b %d, %Y", read_only=True)
    # image = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'

    
    # def get_image_url(self, obj):
    #     if obj.image:
    #         return self.context['request'].build_absolute_uri(obj.image.url)
    #     return None


