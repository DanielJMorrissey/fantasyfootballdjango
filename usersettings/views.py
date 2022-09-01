from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def settings(request):
  template = loader.get_template('usersettings.html')
  return HttpResponse(template.render())