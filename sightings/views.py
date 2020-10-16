from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Squirrel
from .forms import TrackingForm

def squirrels_list(request):
  squirrels = Squirrel.objects.all()
  context = {'squirrels': squirrels}
  return render(request, 'sightings/squirrel_list.html', context)

def update_squirrel(request, squirrel_id):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID = squirrel_id)
    
    if request.method == 'POST':
        form = TrackingForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            message.success(request, "Updated successfully!")
            return redirect(f'/sightings/')
    else:
        form = TrackingForm(instance=squirrel)
        
    context = {'form':form,}
    return render(request, 'sightings/update.html',context)


