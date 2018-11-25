import datetime
from django.db import models
from extras.models import MiniBaseModel


AREACHOICES = (
    ('', ''),
    ('Northern America', 'Northern America'),
    ('other', 'other part of the world'),
)


class TrapTransmitterOrderModel(MiniBaseModel):
    class Meta:
        db_table = 'trapTransmitterOrderModel'

    world_location = models.CharField(null=True, blank=True, max_length=255, choices=AREACHOICES)
    interval = models.PositiveIntegerField(null=True, blank=True, default=24)

    def __repr__(self):
        return 'trapTransmitter'

    def save(self, *args, **kwargs):
        self.created_at = datetime.datetime.now()
        self.origin = ' § amountTransmitters:' + str(self.number_of_collars) + \
                      ' § VHFrequencies:' + str(self.vhf_beacon_frequency) + \
                      ' § notifiEmail:' + str(self.notification_mail) + ' § notifySms:' + str(self.notification_sms) +\
                      ' § GL:' + str(self.globalstar) + ' § airFeeConName:' + str(self.contact_name_airtime_fee) +\
                      ' § airFeeConMail:' + str(self.contact_mail_airtime_fee) + \
                      ' § location:' + str(self.contact_mail_airtime_fee) + \
                      ' § interval:' + str(self.interval) + \
                      ' § comment:' + str(self.comment) + ' § paymentOpt:' +\
                      str(self.payment_option) + ' § orderNo:' + str(self.order_no) +\
                      ' § asPost:' + str(self.as_post) + ' § asMail:' + str(self.as_email) + ' § createdAt:' +\
                      str(self.created_at) + ' § orderID:' + str(self.operation_Number) + ' § vatEinNumber:' +\
                      str(self.vat_ein_number) + ' § deliveryTime:' + str(self.delivery_time) + '§ inc_or_gmbh:' + str(self.inc_or_gmbh)
        return super(TrapTransmitterOrderModel, self).save(*args, **kwargs)