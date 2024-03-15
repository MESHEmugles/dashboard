from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('name',)
    search_fields = ('status',)
    list_display = ("name","status","created")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('name',)
    search_fields = ('status',)
    list_display = ("name","status","created")
