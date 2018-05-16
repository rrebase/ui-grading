from django.urls import path
from grading import views

urlpatterns = [
    path('', views.index, name="index"),
    path('newgrade', views.newgrade, name="newgrade"),
    path('grades', views.grades, name="grades")
]
