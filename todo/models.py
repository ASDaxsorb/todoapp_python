from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self) -> str:
        return self.title
