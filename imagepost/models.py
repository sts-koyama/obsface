from django.contrib.auth.models import User
from django.db import models


EVALUATION_CHOICES = [('Good', 'Good'), ('Bad', 'Bad')]
class ImageTable(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  post_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  images = models.ImageField(upload_to='')
  useful_review = models.IntegerField(null=True, blank=True, default=0)
  useful_review_record = models.TextField()
  evaluation = models.CharField(max_length=10, choices = EVALUATION_CHOICES)
