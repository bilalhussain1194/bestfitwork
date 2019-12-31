from django import forms
from .models import questions


class questionbankform(forms.ModelForm):

    class Meta:

     model= questions
     fields='__all__'




    def __init__(self,*args,**kwargs):
         super(questionbankform,self).__init__(*args,**kwargs)
         self.fields['category'].empty_label="select"
         self.fields['correct_answer'].empty_label="select"





