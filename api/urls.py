from django.urls import path
from study.views import index, student
urlpatterns = [
    path('index/', index, name='index'),
    path('study/', student,name='Students'),
]