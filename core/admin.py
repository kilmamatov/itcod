from django.contrib import admin
from core import models


@admin.register(models.Appeal)
class Appeal(admin.ModelAdmin):
    list_display = ('number',)


@admin.register(models.Service)
class Appeal(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Declarer)
class Appeal(admin.ModelAdmin):
    list_display = ('name',)
