from django.contrib import admin
from core import models


# @admin.register(models.Appeal)
# class Appeal(admin.ModelAdmin):
#     fields = ['number']
#     search_fields = ['number']
#     list_filter = ('number',)
#
#
# admin.site.register(models.Appeal, Appeal)


@admin.register(models.Appeal)
class Appeal(admin.ModelAdmin):
    list_display = ('number', 'created')
    search_fields = ['number']
    list_filter = ('number',)
    date_hierarchy = 'declarer__age'


@admin.register(models.Service)
class Service(admin.ModelAdmin):
    list_display = ('name',)


class AppealInline(admin.TabularInline):
    model = models.Appeal
    readonly_fields = ['number']


@admin.register(models.Declarer)
class Declarer(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [AppealInline]

