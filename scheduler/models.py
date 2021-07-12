from django.db import models


# Create your models here.
class Scheduler(models.Model):
    def __init__(self):
        self.persons_list = {}
        # self.meetings_list = {}

    def get_persons_list(self):
        return self.persons_list

    def add_person_to_list(self, person):
        self.persons_list[person.get_email()] = person

    # def get_meetings_list(self):
    #     return self.meetings_list
    #
    # def add_meetings_to_list(self, meeting):
    #     self.meetings_list[meeting.get_email()] = meeting


class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.schedule = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email;

    def get_schedule(self):
        return self.schedule


class Meeting(models.Model):
    def __init__(self):
        self.email_list = []

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def get_email_list(self):
        return self.email_list

    def add_email_to_list(self, email):
        self.email_list.append(email)
