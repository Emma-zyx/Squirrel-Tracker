from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
   Latitude = models.FloatField(
       max_length = 255,
       help_text = _('latitude of squirrel')
   )
   Longitude = models.FloatField(
       max_length = 255,
       help_text = _('longtitude of squirrel')
   )
   Unique_Squirrel_ID = models.CharField(
       max_length=255,
       unique = True,
       help_text = _('unique squirrel id'),
       blank = False
   )
   Shift = models.CharField(
       max_length = 255,
       help_text = _('shift of squirrel')
   )
   Date = models.CharField(
       max_length = 255,
       help_text = _('date'),
       blank = True
   )
   Age = models.CharField(
       max_length = 100,
       help_text = _('age of squirrel'),
       blank = True
   )
   Primary_Fur_Color = models.CharField(
       max_length = 255,
       help_text = _('primary fur color of squirrel'),
       blank = True
   )
   Location = models.CharField(
       max_length = 255,
       help_text = _('location of squirrel'),
       blank = True
   )
   Specific_Location = models.CharField(
       max_length = 255,
       help_text = _('specific location of squirrel'),
       blank = True
   )
   Running = models.BooleanField(
       help_text = _('whether or not squirrel is running'),
       blank = True
   )
   Chasing = models.BooleanField(
       help_text = _('whether or not squirrel is squirrel'),
       blank = True
   )
   Climbing = models.BooleanField(
       help_text = _('whether or not squirrel is climbing'),
       blank = True
   )
   Eating = models.BooleanField(
       help_text = _('whether or not squirrel is eating'),
       blank = True
   )
   Foraging = models.BooleanField(
       help_text = _('whether or not squirrel is foraging'),
       blank = True
   )
   Other_Activities = models.CharField(
       max_length = 255,
       help_text = _('other activities of squirrel'),
       blank = True
   )
   Kuks = models.BooleanField(
       help_text = _('whether or not squirrel kuks'),
       blank = True
   )
   Quaas = models.BooleanField(
       help_text = _('whether or not squirrel quaas'),
       blank = True
   )
   Moans = models.BooleanField(
       help_text = _('whether or not squirrel moans'),
       blank = True
   )
   Tail_Flags = models.BooleanField(
       help_text = _('whether or not squirrel tail flags'),
       blank = True
   )
   Tail_Twitches = models.BooleanField(
       help_text = _('whether or not squirrel tail twitches'),
       blank = True
   )
   Approaches = models.BooleanField(
       help_text = _('whether or not squirrel approaches'),
       blank = True
   )
   Indifferent = models.BooleanField(
       help_text = _('whether or not squirrel is indifferent'),
       blank = True
   )
   Runs_From = models.BooleanField(
       help_text = _('whether or not squirrel runs from'),
       blank = True
   )
   def __str__(self):
      return self.Unique_Squirrel_ID

