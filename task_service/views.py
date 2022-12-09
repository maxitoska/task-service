from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from task_service.models import Task, Tags


def index(request):
    """View function for the home page of the site."""

    tasks = Task.objects.all()
    tags = Tags.objects.all()
    context = {
        "tasks": tasks,
        "tags": tags
    }

    return render(request, "task_service/index.html", context=context)


class TagsCreateView(generic.CreateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("task_service/index.html")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task_service:index")


class TagsUpdateView(generic.UpdateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("task_service:index")


class TagsDeleteView(generic.DeleteView):
    model = Tags
    success_url = reverse_lazy("task_service:index")


class TagsListView(generic.ListView):
    model = Tags
    context_object_name = "tags_list"
    template_name = "task_service/tags_list.html"


def complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.confirmation = not task.confirmation
    task.save()

    return HttpResponseRedirect(reverse("task_service:index"))


def undo(request, pk):
    task = Task.objects.get(pk=pk)
    task.confirmation = not task.confirmation
    task.save()

    return HttpResponseRedirect(reverse("task_service:index"))
