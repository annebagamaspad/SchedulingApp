from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from rest_framework.decorators import api_view

from .models import Scheduler, Person, Meeting
from .scheduler_util import add_meeting, get_available_timeslots, get_schedule, to_json, get_json_available_timeslots

# Create your views here.

scheduler_data = Scheduler()


def index(request):
    return HttpResponse('Hello, world. You\'re at the scheduler index page.')

@api_view(['POST'])
def create_person(request, name, email):
    if email not in scheduler_data.get_persons_list().keys():
        scheduler_data.add_person_to_list(Person(name, email))
        return HttpResponse('Successfully added person: ' + name + ', ' + email, status=200)
    else:
        return HttpResponse('Adding person failed; ' + email + ' already exists.', status=400)


@api_view(['POST'])
def create_meeting(request, format=None):
    email_list = []
    if request.method == 'POST':
        json_data = json.loads(request.body)  # request.raw_post_data w/ Django < 1.4
        try:
            time = json_data['time']
            email_list = json_data['email_list']
        except KeyError:
            HttpResponseServerError("Malformed data!")

    # get available timeslots to check for conflict
    available_timeslots = get_available_timeslots(scheduler_data, email_list)

    if time not in available_timeslots:
        return HttpResponse('Creating meeting failed; one or more attendees are busy at the given timeslot.', status=400)

    meeting = Meeting()
    meeting.set_time(time)

    for email in email_list:
        add_meeting(scheduler_data, email, time)
        meeting.add_email_to_list(email)

    return HttpResponse('Successfully created meeting at ' + str(time) + ':00', status=200)

@api_view(['GET'])
def show_schedule(request, email):
    return JsonResponse(to_json(get_schedule(scheduler_data, email)), safe=False, status=200)

@api_view(['GET'])
def check_available_timeslots(request, format=None):
    email_list = []
    if request.method == 'GET':
        json_data = json.loads(request.body)  # request.raw_post_data w/ Django < 1.4
        try:
            email_list = json_data['email_list']
        except KeyError:
            HttpResponseServerError("Malformed data!")

    return JsonResponse(to_json(get_json_available_timeslots(scheduler_data, email_list)), safe=False, status=200)
