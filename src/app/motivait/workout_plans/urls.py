from django.urls import path
from workout_plans import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weekdays/', views.weekdays, name='weekdays'),
    path('calendar/', views.calendar, name='calendar'),
]
