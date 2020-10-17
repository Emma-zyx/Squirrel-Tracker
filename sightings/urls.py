
from django.urls import path,re_path
from . import views

apps_name = 'sightings'

urlpatterns = [
   path('sightings/', views.squirrels_list, name = 'squirrels_list'),
   re_path(r'^sightings/([0-9]+[A-Z]{1}-[A-Z]{2}-[0-9]{4}-[0-9]+)/$', views.update_squirrel, name='update'),
   path('map/',views.map),
   path('sightings/add/', views.add),
   path('sightings/stats/',views.stats),
]
