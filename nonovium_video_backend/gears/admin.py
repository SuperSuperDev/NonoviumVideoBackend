from django.contrib import admin

from .models import GearFile

# Register your models here.


@admin.register(GearFile)
class GearFileAdmin(admin.ModelAdmin):
    list_display = ("gear_id", "user", "file")
    fields = ("user", "file")
