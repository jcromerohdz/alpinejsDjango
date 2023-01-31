from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('people/', views.people, name="people"),
]