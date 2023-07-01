from django.db import models
from home.models import FeatureContent
# Create your models here.

class ApplContent(FeatureContent):
   button_text = models.CharField(blank=True, max_length=50)
   load_file = models.FileField(blank=True, null=True)
