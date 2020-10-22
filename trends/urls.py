from django.urls import path
from trends import views

urlpatterns = [
    path('', views.home, name='home')
]
