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
    answer_choices=(("A","A"),("B","B"),("C","C"),("D","D"))
    category_type= (
    ("english", "english"), ("urdu", "urdu"), ("math", "math"))

    category=models.CharField(max_length=100,choices=category_type)
    question=models.CharField(max_length=200,default="")


    A=models.CharField(max_length=100,blank=True)
    B = models.CharField(max_length=100,blank=True)
    C = models.CharField(max_length=100,blank=True)
    D = models.CharField(max_length=100,blank=True)
    correct_answer = models.CharField(max_length=2,choices=answer_choices)


