from django.urls import path
from . import views

urlpatterns = [
    path('attacks/', views.attacksPage, name='attacks'),

]
