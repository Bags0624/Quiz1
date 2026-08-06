from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name