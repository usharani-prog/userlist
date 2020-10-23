from django.contrib import admin


# Register your models here.
from . import models


admin.site.register(models.usernames)
admin.site.register(models.activity_periods1)
