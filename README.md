# SchedulingApp API Endpoints:

## CreatePerson
Creates a person given a name and unique email address.

*Will not create a person for an existing email address.
#### POST Request format: <server_ipaddress>:<port>/scheduler/CreatePerson/<name: String>/<email: String>/

## CreateMeeting
Creates a meeting given a list of names and unique email address.
*Will not create a person if at least one attendee is unavailable at the given timeslot.
#### POST Request Parameter format: <server_ipaddress>:<port>/scheduler/CreateMeeting/
  Body:
```
[
  "email_list": [<email: string list>],
	"time": <hour: int>
]
```

## ShowSchedule
Shows the schedule of a person given an email address.
#### GET Request format: <server_ipaddress>:<port>/scheduler/ShowSchedule/<email: String>

## GetAvailableTimeslots/
Shows the schedule of a person given an email address.
#### GET Request format: <server_ipaddress>:<port>/scheduler/GetAvailableTimeslots/
  Body:
```
  {
	  "email_list": [<email: string list>]
  }
```
