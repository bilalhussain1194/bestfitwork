from . import views
from django.urls import  path


urlpatterns=[
    path('',views.home),
    path('home',views.home),
    path('questionbank',views.viewquestions,name='select_questions'),
    path('result',views.Result,name='show_result_page'),
    path('enterquestions',views.enterquestions,name='insert_questions'),
    path('<int:id>',views.enterquestions,name='update_question'),
    path('delete/<int:delete_id>',views.deletequestion,name='delete_question')

]