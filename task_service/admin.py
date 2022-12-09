from django.contrib import admin
from .models import Task, Tags

admin.site.register(Tags)
admin.site.register(Task)

