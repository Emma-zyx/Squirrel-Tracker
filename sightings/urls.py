from django.urls import path
from . import views

apps_name = 'sightings'

urlpatterns = [
   path('sightings/', views.squirrels_list, name = 'squirrels_list'),
   path('sightings/<str:squirrel_id>/', views.update_squirrel, name='update'),
]

