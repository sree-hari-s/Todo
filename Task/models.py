from django.db import models

# Create your models here.
class Task(models.Model):
    Task=models.CharField(max_length=250)
    Is_Completed=models.BooleanField(default=False)
    Created_Date=models.DateField(auto_now_add=True)
    Modified_Date=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.Task