from django.db import models

class Testimony(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    project = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
