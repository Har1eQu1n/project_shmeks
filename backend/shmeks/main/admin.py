from django.contrib import admin
from .models import *
# Register your models here.
class TicketsShopAdmin(admin.ModelAdmin):
    pass

class ReleasesAdmin(admin.ModelAdmin):
    pass

class MerchAdmin(admin.ModelAdmin):
    pass

admin.site.register(TicketsShop, TicketsShopAdmin)
admin.site.register(Releases, ReleasesAdmin)
admin.site.register(Merch, MerchAdmin)
