"""Controller to manage manipulation of measurement schedules."""

__author__ = ('markjin@umich.edu (Zhongjun Jin), ')


from gspeedometer import model
from google.appengine.api import users

def schedule(add_to_schedule_form):


  params = dict()
  thetype = add_to_schedule_form.cleaned_data['type']

  # extract supported fields
  for field in measurement.field_to_description.keys():
    value = add_to_schedule_form.cleaned_data[field]
    if value:
      params[field] = value
  tag = add_to_schedule_form.cleaned_data['tag']
  thefilter = add_to_schedule_form.cleaned_data['filter']
  count = add_to_schedule_form.cleaned_data['count'] or -1
  interval = add_to_schedule_form.cleaned_data['interval']
  priority = add_to_schedule_form.cleaned_data['priority']
  p1 = add_to_schedule_form.cleaned_data['profile_1_freq']
  p2 = add_to_schedule_form.cleaned_data['profile_2_freq']
  p3 = add_to_schedule_form.cleaned_data['profile_3_freq']
  p4 = add_to_schedule_form.cleaned_data['profile_4_freq']

  num_ue = add_to_schedule_form.cleaned_data['#_of_UEs']
  start_time = add_to_schedule_form.cleaned_data['start_time'] 
  end_time = add_to_schedule_form.cleaned_data['end_time']

  time_created = datetime.datetime.utcnow()
  cur_user = users.get_current_user()
  mytype = thetype

  for ue_id in range(numberOfUE):
    task = model.Task()
    task.created = time_created
    task.user = cur_user
    task.type = mytype
    if tag:
      task.tag = tag
    if thefilter:
      task.filter = thefilter
    task.count = count
    task.interval_sec = float(interval)
    task.priority = priority

    # Set up correct type-specific measurement parameters        
    for name, value in params.items():
      setattr(task, 'mparam_' + name, value)
    task.put()


