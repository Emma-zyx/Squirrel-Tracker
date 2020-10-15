from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Squirrel

def squirrels_list(request):
  squirrels = Squirrel.objects.all()
  context = {'squirrels': squirrels}
  return render(request, 'sightings/squirrel_list.html', context)

