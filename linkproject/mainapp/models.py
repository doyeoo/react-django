from pyexpat import model
from django.db import models

class Review(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField(auto_now=True)