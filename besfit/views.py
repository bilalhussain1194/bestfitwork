from django.shortcuts import render,redirect
import matplotlib.pyplot as plt
from django.http import HttpResponse, HttpResponseRedirect
from .models import result,questions
from .questionbankform import questionbankform

def home(request):
    return (render(request,'home.html'))

def viewquestions(request):
    context={'questions':questions.objects.all()}
    return (render(request,'questionbank.html',context))

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



