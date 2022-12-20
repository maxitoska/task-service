from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("task_service.urls", namespace="task_service")),
]
app_name = "task_service"
