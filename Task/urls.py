from django.urls import path,include
from . import views

urlpatterns = [
    path('addTask',views.addTask,name='addTask'),
    path('completedTask/<int:pk>',views.completedTask,name='completedTask'),
    path('notcompletedTask/<int:pk>',views.notcompletedTask,name='notcompletedTask'),
    path('editTask/<int:pk>',views.editTask,name='editTask'),
    path('deleteTask/<int:pk>',views.deleteTask,name='deleteTask'),
]