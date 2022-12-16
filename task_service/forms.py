from django import forms


from task_service.models import Task


class TaskForm(forms.ModelForm):
    optional_deadline = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(
            attrs={"type": "datetime-local"}
        ),
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
