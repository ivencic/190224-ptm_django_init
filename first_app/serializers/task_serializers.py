from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from datetime import datetime

from first_app.models.task import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline']


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_deadline(self, value):
        if value < datetime.now():
            raise ValidationError('The deadline cannot be in the past.')
        return value
