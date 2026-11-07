from django.contrib import admin

from .models import City, Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]
    search_fields = ["name"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "region", "population", "area_km2", "density"]
    list_filter = ["region"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ["name"]}