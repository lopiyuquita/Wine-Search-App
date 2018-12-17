
# Register your models here.
from django.contrib import admin

import winesearch.models as models


admin.site.register(models.Country)
admin.site.register(models.Province)
admin.site.register(models.Region1)
admin.site.register(models.Region2)
admin.site.register(models.Taster)
admin.site.register(models.Variety)
admin.site.register(models.Wine)
admin.site.register(models.Winery)

