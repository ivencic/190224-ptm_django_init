from django.contrib import admin

from first_app.models.choice import STATUS_CHOISES
from first_app.models.task import Task
from first_app.models.subtask import Subtask
from first_app.models.category import Category


# admin.site.register(Task)
# admin.site.register(Subtask)
# admin.site.register(Category)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ...


@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
