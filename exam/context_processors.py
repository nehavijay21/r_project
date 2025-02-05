from django.contrib.auth.models import Group

def is_chief(request):
  return{'is_chief':request.user.groups.filter(name='Chief').exists()}

def is_teacher(request):
  return{'is_teacher':request.user.groups.filter(name='Teacher').exists()}