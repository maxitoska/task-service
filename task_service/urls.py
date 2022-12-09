from django.urls import path

from task_service.views import (
    index, TaskCreateView, TagsUpdateView, TagsDeleteView, complete, undo, TagsCreateView, TagsListView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tags/",
        TagsListView.as_view(),
        name="tags-list",
    ),
    path(
        "tags/create/",
        TagsCreateView.as_view(),
        name="tags-create"
    ),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "<int:pk>/update/",
        TagsUpdateView.as_view(),
        name="tags-update",
    ),
    path(
        "<int:pk>/delete/",
        TagsDeleteView.as_view(),
        name="tags-delete",
    ),
    path(
        "complete/<int:pk>/",
        complete,
        name="complete",
    ),
    path(
        "undo/<int:pk>/",
        undo,
        name="undo",
    ),
]

app_name = "task_service"
