from django.contrib import admin
from .models import ContactContent
from home.admin import HeaderAdmin
# Register your models here.

admin.site.register(ContactContent,HeaderAdmin)
