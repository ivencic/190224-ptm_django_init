from rest_framework import serializers
from first_app.models.category import Category
from rest_framework.exceptions import ValidationError


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        """
        Проверка уникальности названия категории.
        """
        if Category.objects.filter(name=value).exists():
            raise ValidationError('Category with this name already exists.')
        return value

    def create(self, validated_data):
        """
        Создание категории с проверкой уникальности названия.
        """
        name = validated_data.get('name')
        if Category.objects.filter(name=name).exists():
            raise ValidationError('Category with this name already exists.')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Обновление категории с проверкой уникальности названия.
        """
        name = validated_data.get('name')
        if Category.objects.filter(name=name).exclude(pk=instance.pk).exists():
            raise ValidationError('Category with this name already exists.')
        return super().update(instance, validated_data)