from . import views
from django.urls import  path


urlpatterns=[
    path('',views.home),
    path('home',views.home),
    path('reporting',views.reporting),
    path('result',views.result)

]