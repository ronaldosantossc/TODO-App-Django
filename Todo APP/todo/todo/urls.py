from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.Tasklist,name='task-list'),
    path('task/<int:id>', views.taskView,name='task-View'),
    path('newtask/', views.newTask,name='new-task'),
    path('edit/<int:id>',views.editTask,name='edit-task'),
    path('delete/<int:id>', views.deleteTask,name='delete-task'),
    path('yourname/<str:name>', views.yourName,name='your-name')
]

