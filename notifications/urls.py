from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications_list, name='notifications'),
    path('mark-read/<int:pk>/', views.mark_as_read, name='mark_read'),
]