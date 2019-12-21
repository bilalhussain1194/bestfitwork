from django.db import models

from django.db import  models

class result(models.Model):
    category=models.CharField(max_length=200)
    user_name=models.CharField(max_length=200)
    user_email=models.CharField(max_length=200)
    total_questions=models.IntegerField(default=0)
    question_attempt=models.IntegerField(default=0)
    correct_answers=models.IntegerField(default=0)
class questions(models.Model):

    category_type= (
    ("english", "english"), ("urdu", "urdu"), ("math", "math"))

    category=models.CharField(max_length=100,choices=category_type)
    question=models.CharField(max_length=200,default="")


    option1=models.CharField(max_length=100,blank=True,null=True)
    option2 = models.CharField(max_length=100,blank=True,null=True)
    option3 = models.CharField(max_length=100,blank=True,null=True)
    option4 = models.CharField(max_length=100,blank=True,null=True)
    correct_answer = models.IntegerField()


