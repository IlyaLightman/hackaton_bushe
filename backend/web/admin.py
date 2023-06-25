from django.contrib import admin

from web.models import *

# Register your models here.
admin.site.register(Hub)
admin.site.register(Courier)
admin.site.register(Order)
admin.site.register(Waybill)