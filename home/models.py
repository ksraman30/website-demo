from django.db import models

# Create your models here.

class SiteContent(models.Model):
   title_text = models.CharField(blank=True, max_length=100)
   main_text = models.TextField(blank=True, max_length=2000)
   image = models.ImageField(blank=True, null=True)
   class Meta:
      abstract = True

   def __str__(self):
      return self.title_text + ' (' + str(self.id) + ')'

class FeatureContent(SiteContent):
   subtitle_text = models.TextField(blank=True, max_length=100)
   class Meta:
      abstract = True

class CarouselContent(SiteContent):
   button_text = models.CharField(default="Click Here", max_length=50)
   link = models.CharField(default="/", max_length=50)

class HomeContent(FeatureContent):
   button_text = models.CharField(default="Click Here", max_length=50)
   link = models.CharField(default="/", max_length=50)

class GeneralButton(models.Model):
   button_text = models.CharField(default="Click Me", max_length=50)
   load_file = models.FileField()
   class Meta:
      abstract = True
