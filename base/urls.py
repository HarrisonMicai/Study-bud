#for a specific app
from django.urls import path
from . import views

urlpatterns = [
    # Routes
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room")
]