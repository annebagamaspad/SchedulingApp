import json

# def add_person(scheduler_data, person):
#     scheduler_data.add_person_to_list(person)


# def create_meeting(scheduler_data, email_list, time):
#     meeting = Meeting()
#     meeting.add_meeting()
#     meeting.setTime(time)
#
#     for email in email_list:
#         add_meeting(scheduler_data, email, time)
#         meeting.add_email_to_list(email)


def add_meeting(scheduler_data, email, time):
    person = scheduler_data.get_persons_list()[email]
    person.get_schedule().append(time)


def get_schedule(scheduler_data, email):
    schedule = {}

    for i in range(24):
        schedule[str(i) + ':00'] = ''

        if i in scheduler_data.get_persons_list()[email].get_schedule():
            schedule[str(i) + ':00'] += 'In a meeting'

    return schedule
    # return scheduler_data.get_persons_list()[email].get_schedule()


def get_available_timeslots(scheduler_data, email_list):
    busy_slots = []
    available_slots = []

    for email in email_list:
        busy_slots.extend(scheduler_data.get_persons_list()[email].get_schedule())

    # remove duplicates in slots
    busy_slots = list(set(busy_slots))

    for i in range(24):
        if i not in busy_slots:
            available_slots.append(i)

    return available_slots


def get_json_available_timeslots(scheduler_data, email_list):
    available_slots = get_available_timeslots(scheduler_data, email_list)
    formatted_available_slots = []
    for i in available_slots:
        formatted_available_slots.append(str(i) + ':00')

    dict_data = {'free_timeslots': formatted_available_slots}
    return dict_data


def to_json(data):
    data = json.dumps(data)
    return json.loads(data)
