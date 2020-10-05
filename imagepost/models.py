from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Document(models.Model):
  """model for uploaded images (by imagepost)"""
  description = models.CharField(max_length=255, blank=True)
  photo = models.ImageField(upload_to='documents/', default='defo')
  uploaded_at = models.DateTimeField(auto_now_add=True)

EVALUATION_CHOICES = [('Good', 'Good'), ('Bad', 'Bad')]
class ReviewModel(models.Model):
  title = models.CharField(max_length=100)
  
