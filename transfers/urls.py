from django.urls import path
from . import views

urlpatterns = [
    path('', views.transferIn, name='transferIn'),
    path('sell', views.transferOut, name='transferOut'),
]