from django.db import models


# Create your models here.
class Portfolio(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=100)
    link = models.URLField(null=True, blank=True)

    def __str__ (self):
        return self.project_name

class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    summary = models.TextField()
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
