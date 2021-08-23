from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("home")
