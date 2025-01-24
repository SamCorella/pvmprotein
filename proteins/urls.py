from django.urls import path
from . import views

urlpatterns = [
    path('proteins/', views.proteins, name='proteins'),
]