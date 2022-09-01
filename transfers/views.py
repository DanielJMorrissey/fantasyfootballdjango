from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def transferIn(request):
  template = loader.get_template('transferIn.html')
  return HttpResponse(template.render())

def transferOut(request):
  template = loader.get_template('transferOut.html')
  return HttpResponse(template.render())