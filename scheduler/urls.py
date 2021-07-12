from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('CreatePerson/<name>/<email>/', views.create_person),
    path('CreateMeeting/', views.create_meeting),
    path('ShowSchedule/<email>/', views.show_schedule),
    path('GetAvailableTimeslots/', views.check_available_timeslots),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
