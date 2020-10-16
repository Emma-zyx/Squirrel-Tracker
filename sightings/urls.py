
from django.urls import path
from . import views

apps_name = 'sightings'

urlpatterns =[
   path('sightings/', views.squirrels_list, name = 'squirrels_list'),
   path('map/',views.map),
   path('sightings/add/', views.add),
   path('sightings/stats/',views.stats),
]
