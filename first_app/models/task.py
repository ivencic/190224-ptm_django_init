from django.db import models
from rest_framework.authtoken.admin import User

from first_app.models.choice import Status


class Task(models.Model):
    title = models.CharField(max_length=135, unique_for_date='created_at')
    description = models.TextField()
    categories = models.ManyToManyField('Category', related_name='tasks')
    status = models.CharField(max_length=15, choices=Status)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'
        ordering = ('-created_at',)
        verbose_name = 'TASK'
        unique_together = ('title',)
        verbose_name_plural = 'TASKS'
