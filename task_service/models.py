from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    optional_deadline = models.DateTimeField(blank=True, null=True)
    confirmation = models.BooleanField()
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)

    class Meta:
        ordering = ["optional_deadline"]

    def __str__(self):
        return f"{self.content}" \
               f" {self.datetime}" \
               f" {self.optional_deadline}" \
               f" {self.confirmation}" \
               f" {self.tags.name}"
