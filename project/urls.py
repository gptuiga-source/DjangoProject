from django.urls import path
from . import views

urlpatterns = [
    path('', views.visits_page, name='home')
]