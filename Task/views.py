from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(Task=task)
    return redirect('home')