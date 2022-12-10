from django.contrib import admin
from .models import PassportDatabase

# Register your models here

# admin.site.register(PassportDatabase)

@admin.register(PassportDatabase)
class PassportModel(admin.ModelAdmin):
    list_filter = ('ApplicationNo','Name')
    list_display = ('ApplicationNo','Name')
    ordering = ('ApplicationNo',)
 
