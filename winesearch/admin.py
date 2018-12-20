
# Register your models here.
from typing import List

from django.contrib import admin

import winesearch.models as models


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ['country_name']
    list_display = ['country_name']
    ordering = ['country_name']

@admin.register(models.Province)
class ProvinceAdmin(admin.ModelAdmin):
    fields = ['province_name', 'country']
    list_display = ['province_name', 'country']
    ordering = ['province_name']

@admin.register(models.Region1)
class Region1Admin(admin.ModelAdmin):
    fields = ['region1_name', 'province']
    list_display = ['region1_name', 'province']
    ordering = ['region1_name']

@admin.register(models.Region2)
class Region2Admin(admin.ModelAdmin):
    fields = ['region2_name', 'region1']
    list_display = ['region2_name', 'region1']
    ordering = ['region2_name']

@admin.register(models.Variety)
class VarietyAdmin(admin.ModelAdmin):
    fields = ['variety_name']
    list_display = ['variety_name']
    ordering = ['variety_name']

@admin.register(models.Wine)
class WineAdmin(admin.ModelAdmin):
    fields = ['wine', 'description', 'designation', 'price', 'country', 'province', 'region1', 'region2', 'variety']
    list_display = ['wine', 'description', 'designation', 'price', 'country', 'province', 'region1', 'region2', 'variety']
    ordering = ['wine']


@admin.register(models.Winery)
class WineryAdmin(admin.ModelAdmin):
    fields = ['winery_name']
    list_display = ['winery_name']
    ordering = ['winery_name']


@admin.register(models.Taster)
class TasterAdmin(admin.ModelAdmin):
    fields = ['taster_name', 'twitter_handles', 'points']
    list_display = ['taster_name', 'twitter_handles', 'points']
    ordering = ['taster_name']


