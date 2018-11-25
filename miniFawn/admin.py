from django.contrib import admin

from miniFawn.models import MiniFawnOrderModel


class MiniFawnAdmin(admin.ModelAdmin):
    list_display = (
        'operation_Number', 'number_of_collars', 'delivery_addresse', 'origin',
    )


admin.site.register(MiniFawnOrderModel, MiniFawnAdmin)