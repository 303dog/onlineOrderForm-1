from django.contrib import admin
from orderContact.models import OrderContactInvoiceAddresse
from orderContact.models import OrderContactDeliveryAddresse


class OrderContactInvoiceAdmin(admin.ModelAdmin):
    list_display = [
        'organisation_name', 'city', 'zip_code', 'contact_person',
    ]


class OrderContactDeliveryAdmin(admin.ModelAdmin):
    list_display = [
        'delivery_organisation_name', 'delivery_city', 'delivery_zip_code', 'delivery_contact_person',
    ]


admin.site.register(OrderContactInvoiceAddresse, OrderContactInvoiceAdmin)
admin.site.register(OrderContactDeliveryAddresse, OrderContactDeliveryAdmin)