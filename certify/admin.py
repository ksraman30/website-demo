from django.contrib import admin
from .models import CertifyContent
from .models import CertifyHeader
from home.admin import ContentAdmin
from home.admin import HeaderAdmin
# Register your models here.

admin.site.register(CertifyHeader,HeaderAdmin)
admin.site.register(CertifyContent,ContentAdmin)
