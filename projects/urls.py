from django.urls import path
from . import views

urlpatterns = [
    path('', views.projectsPage, name='projects'),
    path('projects/', views.projectsPage, name='projects'),
    path('project/<str:pk>', views.projectPage, name='project'),
]
