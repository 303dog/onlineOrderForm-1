from django.contrib import admin
from .models import LinkHash


# Register your models here.
class HashAdmin(admin.ModelAdmin):
    list_display = ['pk', 'hash']


admin.site.register(LinkHash, HashAdmin)