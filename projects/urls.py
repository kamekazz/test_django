from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.projectsPage, name='projects'),
    path('product/<str:pk>', views.projectPage, name='single-project'),
]
