from django.db import models

from django.db import  models

class result(models.Model):
    category=models.CharField(max_length=200)
    user_name=models.CharField(max_length=200)
    user_email=models.CharField(max_length=200)
    total_questions=models.IntegerField(default=0)
    question_attempt=models.IntegerField(default=0)
    correct_answers=models.IntegerField(default=0)