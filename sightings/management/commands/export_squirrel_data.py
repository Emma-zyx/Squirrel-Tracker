import csv
from sightings.models import Squirrel
from 
from django.core.management import BaseCommand




class Command(BaseCommand):
   help = 'Export squirrel data from  database'

   def add_arguments(self, parser):
        parser.add_argument('squirrel_file', type=str)

   def handle(self, *args, **options):
       file_ = options['squirrel_file']
       with open(file_, 'w') as f:
           attributes = ['Latitude','Longitude','Unique_Squirrel_ID','Shift','Date','Age','Primary_Fur_Color','Location',
                        'Specific_Location','Running','Chasing','Climbing','Eating','Foraging','Other_Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail_Flags',
                        'Tail_Twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs_From']

