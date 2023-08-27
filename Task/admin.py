from django.contrib import admin
from .models import *
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('Task','Is_Completed','Created_Date','Modified_Date')
    search_fields=('Task',)
    
admin.site.register(Task,TaskAdmin)