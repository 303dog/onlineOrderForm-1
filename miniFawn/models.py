import datetime
from django.db import models
from django.urls import reverse
from extras.models import BaseModelWithoutBeltDesign


class MiniFawnOrderModel(BaseModelWithoutBeltDesign):
    class Meta:
        db_table = 'miniFawnOrderModel'

    min_belt_circumference = models.CharField(null=True, blank=True, max_length=100)
    max_belt_circumference = models.CharField(null=True, blank=True, max_length=100)
    skip_count = models.CharField(null=True, blank=True, max_length=255)

    def __repr__(self):
        return 'miniFawn'

    def save(self, *args, **kwargs):
        self.battery_size = '1C'
        self.created_at = datetime.datetime.now()
        has_uploded_contract = True if self.airtime_contract else False
        self.origin = 'animalSpecies:' + str(self.animal_species) +' § batteryType:' + str(self.battery_size) +\
                      ' § amountCollars:' + str(self.number_of_collars) + ' § minCircum:' + str(self.min_belt_circumference) +\
                      ' § maxCircum:' + str(self.max_belt_circumference) + \
                      ' § VHFrequencies:' + str(self.vhf_beacon_frequency) + ' § mortDelay:' + str(self.mortality_sensor) +\
                      ' § notifiEmail:' + str(self.notification_mail) + ' § notifySms:' + str(self.notification_sms) +\
                      ' § timezone:' + str(self.utc_lmt) + ' § utcCorrect:' + str(self.utc_correction) + ' § gpsSched:' +\
                      str(self.gps_schedule) + ' § vhfSched:' + str(self.vhf_beacon_schedule) + ' § idTag:' + str(self.id_tag) +\
                      ' § GL:' + str(self.globalstar) + ' § airFeeConName:' + str(self.contact_name_airtime_fee) +\
                      ' § airFeeConMail:' + str(self.contact_mail_airtime_fee) + ' § uplodedContract:' + str(has_uploded_contract) +\
                      ' § cottonSpacer:' + str(self.cotton_layers) + ' § comment:' + str(self.comment) + ' § paymentOpt:' +\
                      str(self.payment_option) + ' § orderNo:' + str(self.order_no) +\
                      ' § asPost:' + str(self.as_post) + ' § asMail:' + str(self.as_email) + ' § createdAt:' +\
                      str(self.created_at) + ' § orderID:' + str(self.operation_Number) + ' § vatEinNumber:' +\
                      str(self.vat_ein_number) + ' § deliveryTime:' + str(self.delivery_time) + '§ inc_or_gmbh:' + str(self.inc_or_gmbh)
        super(MiniFawnOrderModel, self).save(*args, **kwargs)
