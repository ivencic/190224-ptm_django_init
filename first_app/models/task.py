from django.db import models
from first_app.models.choice import STATUS_CHOISES


class Task(models.Model):
    title = models.CharField(max_length=135, unique_for_date='created_at')
    description = models.TextField()
    categories = models.ManyToManyField('Category', related_name='tasks')
    status = models.CharField(max_length=15, choices=STATUS_CHOISES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'
        ordering = ('-created_at',)
        verbose_name = 'TASK'
        unique_together = ('title',)
        verbose_name_plural = 'TASKS'
