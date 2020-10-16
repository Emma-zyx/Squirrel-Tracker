from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Squirrel
from random import sample

def squirrels_list(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'sightings/squirrel_list.html', context)

def map(request):
    random_100 = random.sample(range(squirrels.objects.all().count()),k=100)
    mapped = []
    for i in random_100:
        mapped.append(squirrels.objects.all()[i])
    context = {'sightings': mapped}
    return render(request, 'sightings/map.html',context)
