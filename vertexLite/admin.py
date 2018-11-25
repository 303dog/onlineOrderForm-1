from django.contrib import admin
from vertexLite.models import VertexLiteOrderModel


class VertexLiteAdmin(admin.ModelAdmin):
    list_display = (
        'operation_Number', 'number_of_collars', 'delivery_addresse', 'origin',
    )


admin.site.register(VertexLiteOrderModel, VertexLiteAdmin)