from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
  template = loader.get_template('canvas/index.html')
  context = { 'name': 'Alexey' }
  return HttpResponse(
    template.render(context, request)
  )
