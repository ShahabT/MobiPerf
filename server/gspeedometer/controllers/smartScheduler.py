"""Controller to manage manipulation of measurement schedules."""
from datetime import datetime

__author__ = ('markjin@umich.edu (Zhongjun Jin), tajik@umich.edu (Shahab Tajik)')

from gspeedometer import model
from google.appengine.api import users


def schedule(task, start, end, count):
    group = model.TaskGroup()
    group.start_time = datetime.strptime(start, "%m-%d-%Y %H:%M")
    group.end_time = datetime.strptime(end, "%m-%d-%Y %H:%M")
    group.deviceCount = count
    group.doneCount = 0
    group.put()
    task.group = group
    for i in range(0, count):
        t = model.Task()
        t.group = task.group
        t.count = task.count
        t.created = task.created
        t.filter = task.filter
        t.tag = task.tag
        t.interval_sec = task.interval_sec
        t.priority = task.priority
        t.start_time = task.start_time
        t.end_time = task.end_time
        t.user = task.user
        t.type = task.type
        for name, value in task.Params().items():
            setattr(t, 'mparam_' + name, value)
        t.put()


def getDeviceSchedule(device_info):
    groups = model.TaskGroup.all().filter("deviceCount < doneCount")
    matched = set()
    for group in groups:
        matched.add(group.getTasksForDevice(device_info))
    return matched