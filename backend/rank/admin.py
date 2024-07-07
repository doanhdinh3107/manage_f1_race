from django.contrib import admin
from . import models



@admin.register(models.Team)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','point',)

admin.site.register(models.GrandBahrain)

admin.site.register(models.GrandAustralia)

admin.site.register(models.GrandJapan)

@admin.register(models.Racer)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','team','birth',"point",)