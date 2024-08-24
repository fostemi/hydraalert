from django.urls import path
from workout_plans import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('weekdays/', views.weekdays, name='weekdays'),
    path('calendar-body/', views.get_calendar_body, name='calendar_body'),
    path('calendar/', views.get_calendar, name='calendar'),
]
