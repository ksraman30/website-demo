from django.contrib import admin
from .models import CertContent
from .models import ProductContent
from .models import UsesContent
from .models import ProductButton
from home.admin import ContentAdmin
# Register your models here.

admin.site.register(CertContent,ContentAdmin)
admin.site.register(ProductContent,ContentAdmin)
admin.site.register(UsesContent,ContentAdmin)
admin.site.register(ProductButton,ContentAdmin)
