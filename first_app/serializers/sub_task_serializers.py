from rest_framework import serializers
from first_app.models.subtask import Subtask


class SubTaskCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Subtask
        fields = '__all__'
        read_only_fields = ('created_at', )


class SubTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Subtask
        fields = '__all__'
