from django.core.management import BaseCommand
from sightings.models import Squirrel
import csv, re, datetime

class Command(BaseCommand):
    help = 'Get squirrel data into database'
   
    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help='file containing squirrel details')
   
    def handle(self, *args, **options):
        file_ = options['squirrel_file']
        pattern = re.compile(r'([0-9]{2})([0-9]{2})([0-9]{4})')
       
        with open(file_) as fp:
            reader = csv.reader(fp)
            next(reader)
            unique_id = []
            for item in reader:
                year = pattern.match(item[5]).groups()[2]
                month = pattern.match(item[5]).groups()[0]
                day = pattern.match(item[5]).groups()[1]
                if item[2] in unique_id:
                    continue
                else:
                    unique_id.append(item[2])
                    for i in (15,16,17,18,19,21,22,23,24,25,26,27,28):
                        if item[i] == 'true':
                            item[i] = True
                        else:
                            item[i] = False
                    squirrel = Squirrel.objects.get_or_create(
                            Latitude = float(item[0]),
                            Longitude = float(item[1]),
                            Unique_Squirrel_ID = item[2],
                            Shift = item[4],
                            Date = datetime.date(int(year), int(month), int(day)),
                            Age = item[7],
                            Primary_Fur_Color = item[8],
                            Location = item[12],
                            Specific_Location = item[14],
                            Running = item[15],
                            Chasing = item[16],
                            Climbing = item[17],
                            Eating = item[18],
                            Foraging = item[19],
                            Other_Activities = item[20],
                            Kuks = item[21],
                            Quaas = item[22],
                            Moans = item[23],
                            Tail_Flags = item[24],
                            Tail_Twitches = item[25],
                            Approaches = item[26],
                            Indifferent = item[27],
                            Runs_From = item[28]
                            )

