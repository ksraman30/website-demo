from django.db import models
from home.models import FeatureContent
from home.models import GeneralButton
# Create your models here.

class ProductContent(models.Model):
   #id is automatic
   readonly_fields = ('id',)
   #title
   title_text = models.CharField(blank=True, max_length=100)
   #accompanying image
   image = models.ImageField(blank=True,null=True)
   #other names
   aka_text = models.CharField(blank=True, max_length=2000)
   #purity
   purity_text = models.CharField(blank=True, max_length=2000)
   #standards
   standards_text = models.CharField(blank=True, max_length=2000)
   #pack sizes
   sizes_text = models.CharField(blank=True, max_length=2000)
   #product specs
   specs_text = models.CharField(blank=True, max_length=2000)
   #uses

   def __str__(self):
      return self.title_text + '(' + str(self.id) +')'

class ProductButton(GeneralButton):
   related_product = models.ForeignKey(ProductContent,on_delete=models.CASCADE)

class UsesContent(models.Model):
   readonly_fields = ('id',)
   use_text = models.CharField(blank=True, max_length=2000)
   related_product = models.ForeignKey(ProductContent,on_delete=models.CASCADE)

   def __str__(self):
      return self.use_text[:30] + ' (' + str(self.id) +')'

class CertContent(FeatureContent):
   pass
