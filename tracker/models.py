from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    applied_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return self.company_name
