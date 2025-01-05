from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    repeat_daily = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title