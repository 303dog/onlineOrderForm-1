from django.contrib import admin

from traptransmitter.models import TrapTransmitterOrderModel


class TrapTransmitterAdmin(admin.ModelAdmin):
    list_display = (
        'operation_Number', 'number_of_collars', 'delivery_addresse', 'origin',
    )


admin.site.register(TrapTransmitterOrderModel, TrapTransmitterAdmin)