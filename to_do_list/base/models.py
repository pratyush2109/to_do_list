from django.db import models
from django.contrib.auth.models import User 

class Task(models.Model):
    # User, which includes Id, Email etc. 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # Title for a task
    title = models.CharField(max_length=200)
    # Description for a task
    description = models.TextField(null=True, blank=True)
    # Determines if the task is complete or not
    complete = models.BooleanField(default=False)
    # Time and date of the created task 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']