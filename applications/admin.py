from django.contrib import admin
from .models import ApplContent
from home.admin import ContentAdmin
# Register your models here.

admin.site.register(ApplContent,ContentAdmin)
