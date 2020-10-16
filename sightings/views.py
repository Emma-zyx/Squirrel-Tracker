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
    random_100 = random.sample(range(Squirrel.objects.all().count()),k=100)
    mapped = []
    for i in random_100:
        mapped.append(Squirrel.objects.all()[i])
    context = {'sightings': mapped}
    return render(request, 'sightings/map.html',context)

def add(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = TrackingForm()
    context = {'form': form}
    return render(request, 'sightings/add.html',context)

def stats(request):
    sq_num = Squirrel.objects.all().count()
    sq_adult = Squirrel.objects.filter(Age='Adult').count()
    sq_cinna = Squirrel.objects.filter(Primary_fur_color='Cinnamon').count()
    sq_chasing = Squirrel.objects.filter(Chasing=True).count()
    sq_tail_twitches = Squirrel.objects.filter(Tail_twitches=True).count()

    context = {'sq_num': sq_num,
               'sq_adult': sq_adult,
               'sq_cinna': sq_cinna,
               'sq_chasing': sq_chasing,
               'sq_tail_twitches': sq_tail_twitches}

    return render(request, 'sightings/stats.html',context)
