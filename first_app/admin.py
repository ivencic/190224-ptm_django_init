from django.contrib import admin

from first_app.models.task import Task
from first_app.models.subtask import Subtask
from first_app.models.category import Category


admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(Category)

