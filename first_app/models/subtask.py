from django.db import models

from first_app.models.choice import STATUS_CHOISES

class Subtask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='subtasks')
    status = models.CharField(max_length=15, choices=STATUS_CHOISES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
