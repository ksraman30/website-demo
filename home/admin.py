from django.contrib import admin
from .models import HomeContent
from .models import CarouselContent
# Register your models here.

class ContentAdmin(admin.ModelAdmin):
   readonly_fields = ('id',)

class HeaderAdmin(ContentAdmin):
   exclude=('image',)

admin.site.register(CarouselContent,ContentAdmin)
admin.site.register(HomeContent,ContentAdmin)
