import datetime
from django.db import models
from extras.utils import BELTCOLORS
from extras.utils import BELTEDGES
from extras.utils import BELTSHAPES
from extras.utils import BELTTHICKNESS
from extras.utils import BELTWIDTH
from extras.utils import PAYMENTOPTIONS
from extras.utils import STAFFS
from extras.utils import UTCORLMT
from orderContact.models import OrderContactInvoiceAddresse
from orderContact.models import OrderContactDeliveryAddresse
from orderForm import settings


def upload_path(instance, filename):
    return '/'.join([settings.MEDIA_ROOT, str(instance.contacts_faktura_id), filename])


def gps_schedule_upload_path(instance, filename):
    return '/'.join([settings.MEDIA_ROOT, str(instance.contacts_faktura_id), 'gps_schedule', filename])


def vhf_schedule_upload_path(instance, filename):
    return '/'.join([settings.MEDIA_ROOT, str(instance.contacts_faktura_id), 'vhf_schedule', filename])


class MiniBaseModel(models.Model):

    class Meta:
        abstract = True

    payment_option = models.CharField(choices=PAYMENTOPTIONS, max_length=255, blank=True, default='check')
    order_no = models.CharField(null=True, blank=True, max_length=255)
    as_post = models.BooleanField(default=False, blank=True)
    as_email = models.BooleanField(default=True, blank=True)
    invoice_mail = models.EmailField(null=True, blank=True)
    number_of_collars = models.CharField(null=True, blank=True, max_length=100)
    customer_faktura_id = models.IntegerField(editable=False, null=True)
    contacts_faktura_id = models.IntegerField(null=True, blank=True)
    customer_invoice_address = models.ForeignKey(OrderContactInvoiceAddresse, null=True, blank=True)
    delivery_addresse = models.ForeignKey(OrderContactDeliveryAddresse, null=True, blank=True)
    same_addr = models.BooleanField(blank=True, default=True)
    globalstar = models.BooleanField(blank=True, default=False)
    iridium = models.BooleanField(blank=True, default=False)
    vhf_beacon_schedule = models.CharField(blank=True, default='24', max_length=255, null=True)
    vhf_beacon_frequency = models.TextField(blank=True, null=True, default=148)
    contact_name_airtime_fee = models.CharField(blank=True, null=True, max_length=255)
    contact_mail_airtime_fee = models.EmailField(blank=True, null=True)
    notification_mail = models.CharField(blank=True, null=True, max_length=500)
    notification_sms = models.CharField(blank=True, null=True, max_length=255)

    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    customer_staff = models.CharField(choices=STAFFS, blank=True, null=True, max_length=255)
    origin = models.TextField(editable=False, null=True, blank=True, max_length=1000)
    order_acceptet = models.BooleanField(default=False)
    operation_Number = models.CharField(max_length=255, blank=True, null=True)
    id_tag = models.BooleanField(blank=True, default=False)
    airtime_contract = models.FileField(blank=True, upload_to=upload_path)
    vat_ein_number = models.CharField(max_length=255, blank=True, null=True, default='')
    delivery_time = models.DateField(blank=True, null=True)
    inc_or_gmbh = models.CharField(blank=True, null=True, default='gmbh', max_length=13)
    owm_gps_schedule = models.FileField(null=True, blank=True, upload_to=gps_schedule_upload_path)
    own_vhf_schedule = models.FileField(null=True, blank=True, upload_to=vhf_schedule_upload_path)


class BaseModelWithoutBeltDesign(MiniBaseModel):

    class Meta:
        abstract = True

    animal_species = models.CharField(max_length=255, blank=True, null=True)
    battery_size = models.CharField(max_length=100, null=True, blank=True)
    nom_collar_circumference = models.TextField(blank=True, null=True, max_length=255)
    mortality_sensor = models.PositiveIntegerField(blank=True, null=True, default=24)
    utc_lmt = models.CharField(blank=True, default=False, max_length=50, choices=UTCORLMT, null=True)
    utc_correction = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    cotton_layers = models.IntegerField(blank=True, null=True)

    gps_schedule = models.CharField(blank=True, default='Every 13h', max_length=255, null=True)
    iridium_num_of_fixes_gps = models.IntegerField(blank=True, null=True)
    iridium_contract_type = models.CharField(max_length=255, null=True, blank=True, default='')


class BaseModel(BaseModelWithoutBeltDesign):

    class Meta:
        abstract = True

    belt_width = models.CharField(choices=BELTWIDTH, blank=True, null=True, max_length=255)
    belt_thickness = models.CharField(choices=BELTTHICKNESS, blank=True, null=True, max_length=255)
    belt_edge = models.CharField(choices=BELTEDGES, blank=True, null=True, max_length=255, default='round')
    belt_colour = models.CharField(choices=BELTCOLORS, blank=True, null=True, max_length=255)
    other_color = models.CharField(max_length=100, blank=True, null=True)
    belt_labeling = models.BooleanField(blank=True, default=False)
    belt_labeling_instructions = models.CharField(max_length=255, null=True, blank=True)
    belt_plates = models.BooleanField(blank=True, default=False)
    belt_plates_instructions = models.CharField(max_length=76, null=True, blank=True)
    belt_shape = models.CharField(choices=BELTSHAPES, max_length=255, blank=True, null=True)

    reflective_stripes = models.BooleanField(blank=True, default=False)
    reflective_stripes_instructions = models.CharField(max_length=76, null=True, blank=True)