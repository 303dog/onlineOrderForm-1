from django.contrib import admin
from .models import SurveyOrderModel
from collar.models import Beltshapes
from collar.models import Beltthickness, Beltedges, Beltcolors

# Register your models here.
class SurveyAdmin(admin.ModelAdmin):
    list_display = [
        'operation_Number', 'number_of_collars', 'delivery_addresse', 'origin', 'pk',
        ]


admin.site.register(SurveyOrderModel, SurveyAdmin)
admin.site.register(Beltshapes)
admin.site.register(Beltthickness)
admin.site.register(Beltedges)
admin.site.register(Beltcolors)
