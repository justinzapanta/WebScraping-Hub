from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in/', views.sign_in, name='sign-in')
]