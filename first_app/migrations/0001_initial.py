# Generated by Django 5.0.6 on 2024-06-02 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=135, unique_for_date='created_at')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('IN PROGRESS', 'IN PROGRESS'), ('PENDING', 'PENDING'), ('BLOCKED', 'BLOCKED'), ('DONE', 'DONE')], max_length=15)),
                ('deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='tasks', to='first_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('IN PROGRESS', 'IN PROGRESS'), ('PENDING', 'PENDING'), ('BLOCKED', 'BLOCKED'), ('DONE', 'DONE')], max_length=15)),
                ('deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='first_app.task')),
            ],
        ),
    ]