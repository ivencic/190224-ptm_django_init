from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'CATEGORY'
        unique_together = ('name',)
        verbose_name_plural = 'CATEGORIES'
