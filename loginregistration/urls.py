from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('login/computelogin', views.computeLogin, name='computelogin'),
    path('register', views.register, name='register'),
    path('register/computeregistration', views.computeregistration, name='computeregistration'),
    path('signout', views.signout, name='signout'),
]