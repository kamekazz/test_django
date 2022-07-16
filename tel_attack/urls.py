from django.urls import path
from . import views

urlpatterns = [
    path('attacks/', views.attacksPage, name='attacks'),
    path('add-tel/', views.addPNPage, name='addPN'),
    path('attack-map/<str:pk>', views.attackMapPage, name='attack-map'),

]
