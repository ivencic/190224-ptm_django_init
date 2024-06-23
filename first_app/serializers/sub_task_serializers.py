from rest_framework import serializers
from first_app.models.subtask import Subtask


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'
        read_only_fields = ('created_at', )
