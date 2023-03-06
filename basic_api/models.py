from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_subject = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
