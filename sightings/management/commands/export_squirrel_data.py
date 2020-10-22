import csv
from sightings.models import Squirrel
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Export squirrel data from database'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', type=str)

    def handle(self, *args, **options):
        file_ = options['squirrel_file']
        with open(file_, 'w') as fp:
            writer = csv.writer(fp)
            titles = [
                    'Latitude', 'Longitude', 'Unique_Squirrel_ID', 
                    'Shift', 'Date', 'Age', 'Primary_Fur_Color', 
                    'Location', 'Specific_Location', 'Running',
                    'Chasing', 'Climbing', 'Eating', 'Foraging',
                    'Other_Activities', 'Kuks', 'Quaas', 'Moans',
                    'Tail_Flags', 'Tail_Twitches', 'Approaches', 
                    'Indifferent', 'Runs_From'
                    ]
           writer.writerow(titles)
           values = Squirrel.objects.all()
           for item in values:
               writer.writerow([
                   item.Longitude, item.Latitude, item.Unique_Squirrel_ID,
                   item.Shift, item.Date, item.Age, item.Primary_Fur_Color,
                   item.Location, item.Specific_Location, item.Running,
                   item.Chasing, item.Climbing, item.Eating,
                   item.Foraging, item.Other_Activities, item.Kuks,
                   item.Quaas, item.Moans, item.Tail_Flags,
                   item.Tail_Twitches, item.Approaches, 
                   item.Indifferent, item.Runs_From
                   ])
