from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Feature)
admin.site.register(models.Device)
admin.site.register(models.Review_device)
