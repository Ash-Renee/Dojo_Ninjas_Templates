from django.urls import path
from . import views

urlpatterns = [

    path('',views.index),
    path('process/student', views.people),
    path('create_dojo', views.building),
]
