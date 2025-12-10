from django.urls import path
from . import views

urlpatterns = [       
    path('', views.home),  

    # CRUD API + UI
    path('list/', views.getTasks),
    path('ui/', views.tasksUI),
    path('create/', views.createTask),          
    path('update/<int:pk>/', views.updateTask),  
    path('delete/<int:pk>/', views.deleteTask),  
   
    # External API + Fetch UI
    path('fetch-indicator/', views.fetch_indicator_dynamic),
    path('fetch-data/', views.fetchDataUI),

    # Visualization
    path('analytics/', views.analyticsDashboard),
    path('load-db-data/', views.load_from_database),
    

]