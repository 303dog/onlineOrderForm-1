import datetime
from django.db import models
from django.urls import reverse
from extras.utils import BELTCOLORS
from extras.utils import BELTEDGES
from extras.utils import BELTSHAPES
from extras.utils import BELTTHICKNESS
from extras.utils import BELTWIDTH
from extras.utils import DROPOFFCONTROLL
from extras.utils import PAYMENTOPTIONS
from extras.utils import STAFFS
from extras.utils import UTCORLMT
from orderContact.models import OrderContactInvoiceAddresse
from orderContact.models import OrderContactDeliveryAddresse
from orderForm import settings
from extras.models import BaseModel


def upload_path(instance, filename):
    return '/'.join([settings.MEDIA_ROOT, str(instance.contacts_faktura_id), filename])


def gps_schedule_upload_path(instance, filename):
    return '/'.join([settings.MEDIA_ROOT, str(instance.contacts_faktura_id), 'gps_schedule', filename])


def vhf_schedule_upload_path(instance, filename):
    return '/'.join([settings.MEDIA_ROOT, str(instance.contacts_faktura_id), 'vhf_schedule', filename])


class SurveyOrderModel(BaseModel):
    class Meta:
        db_table = 'SurveyOrderModel'

    external_dropoff = models.BooleanField(blank=True, default=False)
    external_dropoff_controll = models.CharField(choices=DROPOFFCONTROLL, blank=True, null=True, max_length=200)
    external_dropoff_real_time = models.CharField(blank=True, null=True, max_length=200)
    external_dropoff_abs_time = models.CharField(blank=True, null=True, max_length=200)

    def __repr__(self):
        return 'survey'

    def save(self, *args, **kwargs):
        self.created_at = datetime.datetime.now()
        has_uploded_contract = True if self.airtime_contract else False
        self.origin = 'animalSpecies:' + str(self.animal_species) +' § batteryType:' + str(self.battery_size) +\
                      ' § amountCollars:' + str(self.number_of_collars) + ' § beltCircum:' + str(self.nom_collar_circumference) +\
                      ' § beltShape:' + str(self.belt_shape) + ' § beltWidth:' + str(self.belt_width) + ' § beltTickn:' +\
                      str(self.belt_thickness) + '§ beltEdge:' + str(self.belt_edge) + ' § beltColor:' + str(self.belt_colour) +\
                      ' § otherColor:' + str(self.other_color) + ' § beltLabel:' + str(self.belt_labeling) +\
                      ' § beltLabelIns:' + str(self.belt_labeling_instructions) + ' § beltPlates:' + str(self.belt_plates) +\
                      ' § beltPlatesIns:' + str(self.belt_plates_instructions) + ' § reflectStripes:' + str(self.reflective_stripes) +\
                      ' § VHFrequencies:' + str(self.vhf_beacon_frequency) + ' § mortDelay:' + str(self.mortality_sensor) +\
                      ' § notifiEmail:' + str(self.notification_mail) + ' § notifySms:' + str(self.notification_sms) +\
                      ' § timezone:' + str(self.utc_lmt) + ' § utcCorrect:' + str(self.utc_correction) + ' § gpsSched:' +\
                      str(self.gps_schedule) + ' § vhfSched:' + str(self.vhf_beacon_schedule) + ' § idTag:' + str(self.id_tag) +\
                      ' § GL:' + str(self.globalstar) + ' § IR:' + str(self.iridium) + ' § IRNumOfPos:' +\
                      str(self.iridium_num_of_fixes_gps) + ' § IRContType:' + str(self.iridium_contract_type) +\
                      ' § airFeeConName:' + str(self.contact_name_airtime_fee) + ' § airFeeConMail:' + str(self.contact_mail_airtime_fee) +\
                      ' § uplodedContract:' + str(has_uploded_contract) + ' § dropOff:' + str(self.external_dropoff) +\
                      ' § dropOffContr:' + str(self.external_dropoff_controll) + ' § dropOffRelTime:' +\
                      str(self.external_dropoff_real_time) + ' § dropOffAbsTime:' + str(self.external_dropoff_abs_time) +\
                      ' § cottonSpacer:' + str(self.cotton_layers) + ' § comment:' + str(self.comment) + ' § paymentOpt:' +\
                      str(self.payment_option) + ' § orderNo:' + str(self.order_no) +\
                      ' § asPost:' + str(self.as_post) + ' § asMail:' + str(self.as_email) + ' § createdAt:' +\
                      str(self.created_at) + ' § orderID:' + str(self.operation_Number) + ' § vatEinNumber:' +\
                      str(self.vat_ein_number) + ' § deliveryTime:' + str(self.delivery_time) + '§ inc_or_gmbh:' + str(self.inc_or_gmbh)
        super(SurveyOrderModel, self).save(*args, **kwargs)

    def get_sells_update_url(self, hash):
        return reverse('survey:survey_customer_form', kwargs={'hash': hash,
                                                              'pk': self.pk})

    def get_sells_detail_url(self):
        return reverse('security:detailsurveys', kwargs={'pk': self.pk})
