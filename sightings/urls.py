from django.urls import path
from . import views

apps_name = 'sightings'

urlpatterns = [
   path('', views.squirrels_list, name = 'squirrels_list')
]

