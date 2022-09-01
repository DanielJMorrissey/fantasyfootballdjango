from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def score(request):
  template = loader.get_template('score.html')
  return HttpResponse(template.render())