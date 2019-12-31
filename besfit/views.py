from django.shortcuts import render,redirect
import matplotlib.pyplot as plt
from django.http import HttpResponse, HttpResponseRedirect
from besfit.models import  result,questions
from .questionbankform import questionbankform
from pandas import  DataFrame as dt
import numpy as np
from django.db.models import Case, CharField, Value, When

def home(request):
    return (render(request,'home.html'))

def viewquestions(request):

     # questionall={'questionall':questions.objects.all()}
     questionall={'questionall':questions.objects.annotate(
        correct_answer_option=Case(
            When(correct_answer='A',then="A"),
            When(correct_answer='B',then="B"),
            When(correct_answer='C', then="C"),
            When(correct_answer='D', then="D"),
            output_field=CharField()

        )
    )}
     return render(request,'questionbank.html',questionall)






def Result(request):

   filter_result = result.objects.all()

   return (render(request,'result.html',{'filter_result':filter_result}))
def enterquestions(request,id=0):
  if request.method=="GET":
      if id==0:
          form = questionbankform()

      else:
          questions_update=questions.objects.get(pk=id)
          form = questionbankform(instance=questions_update)

      return render(request, 'enterquestions.html', {'form': form})




  else:
      if id==0:
          form = questionbankform(request.POST)
          if form.is_valid():
              form.save()
          return HttpResponseRedirect("")
      else:
        update_question=questions.objects.get(pk=id)
        form = questionbankform(request.POST,instance=update_question)
      if form.is_valid():
          form.save()
      return redirect('/home/questionbank')


def deletequestion(request,delete_id):
     delete_question=questions.objects.get(pk=delete_id)
     delete_question.delete()
     return redirect('/home/questionbank')




