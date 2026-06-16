from core.views import *
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('change_status/<int:id>/', views.change_status, name='change_status')
]
