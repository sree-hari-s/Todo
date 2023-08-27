from django.http import HttpResponse
from django.shortcuts import render
from Task.models import *

def home(request):
    tasks=Task.objects.filter(Is_Completed=False).order_by('-Modified_Date')
    completed_tasks=Task.objects.filter(Is_Completed=True).order_by('-Modified_Date')
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    }
    return render(request,'home.html',context=context)

