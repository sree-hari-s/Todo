from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(Task=task)
    return redirect('home')

def completedTask(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.Is_Completed=True
    task.save()
    return redirect('home')

def notcompletedTask(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.Is_Completed=False
    task.save()
    return redirect('home')

def editTask(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task=request.POST['newTask']
        get_task.Task=new_task
        get_task.save()
        return redirect('home')
    else:
        context={
            get_task:'get_task'
        }
        return render(request,'edit.html',context=context)
    
def deleteTask(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')