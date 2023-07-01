from django.contrib import admin
from .models import AboutContent
from home.admin import ContentAdmin
# Register your models here.

admin.site.register(AboutContent,ContentAdmin)
