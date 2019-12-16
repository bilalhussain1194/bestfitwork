from django.shortcuts import render
import matplotlib.pyplot as plt
from django.http import HttpResponse

def home(request):
    return (render(request,'home.html'))

def reporting(request):
    return (render(request,'reporting.html'))

def result(request):
    return (render(request,'result.html'))