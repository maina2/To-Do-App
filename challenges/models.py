from django.db import models


class Task(models.Model):
    title = models.CharField(("Task Title"), max_length=50),
    description = models.TextField()
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    
    def __str__(self):
        return self.title
