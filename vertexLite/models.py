import datetime
from django.db import models
from django.utils.timezone import now
from extras.utils import DROPOFFCONTROLL
from orderForm import settings
from extras.models import BaseModel


VERTEXLITEBELTSHAPES = (
    ('round-shaped', 'round-shaped'),
    ('drop-shaped', 'drop-shaped'),
    ('ovalround-shaped', 'ovalround-shaped')
)


def upload_path(instance, filename):
    return '/'.join([settings.MEDIA_ROOT, str(instance.contacts_faktura_id), filename])


class VertexLiteOrderModel(BaseModel):
    class Meta:
        db_table = 'VertexLiteOrderModel'

    belt_shape = models.CharField(choices=VERTEXLITEBELTSHAPES, max_length=255, blank=True, null=True)

    external_dropoff = models.BooleanField(blank=True, default=False)
    external_dropoff_controll = models.CharField(choices=DROPOFFCONTROLL, blank=True, null=True, max_length=200)
    external_dropoff_real_time = models.CharField(blank=True, null=True, max_length=200)
    external_dropoff_abs_time = models.CharField(blank=True, null=True, max_length=200)

    internal_dropoff = models.BooleanField(blank=True, default=False)
    internal_dropoff_controll = models.CharField(choices=DROPOFFCONTROLL, blank=True, null=True, max_length=200)
    internal_dropoff_real_time = models.CharField(blank=True, null=True, max_length=200)
    internal_dropoff_abs_time = models.CharField(blank=True, null=True, max_length=200)

    store_on_board = models.BooleanField(blank=True, default=False)

    gsm = models.BooleanField(blank=True, default=False)
    gsm_vectronic_sim = models.BooleanField(blank=True, default=True)
    gsm_mode = models.CharField(blank=True, null=True, max_length=1, default='8')
    gsm_customer_sim_telephone_no = models.CharField(null=True, blank=True, max_length=9999)
    gsm_customer_sim_pin = models.CharField(null=True, blank=True, max_length=9999)
    gsm_customer_sim_puk = models.CharField(null=True, blank=True, max_length=9999)
    groundstation_number = models.CharField(null=True, blank=True, max_length=255,
                                            help_text='If data should <u><b>not</b></u> be sent to VAS ground station')

    def __repr__(self):
        return 'vertex_lite'

    def __str__(self):
        return 'vertex_lite'

    def save(self, *args, **kwargs):
        if self.gsm_vectronic_sim is not None:
            self.gsm = True
            if self.gsm_vectronic_sim is False:
                self.gsm_mode = '7'
            else:
                self.gsm_mode = '8'
        if not self.order_acceptet and self.animal_species is not None:
            self.created_at = now()
            self.origin = self.payment_option + '§' + str(self.number_of_collars) + '§' + self.battery_size + '§' +\
                          str(self.animal_species) + '§' + str(self.belt_shape) + '§' + str(self.nom_collar_circumference) + '§' +\
                          str(self.vhf_beacon_frequency) + '§' + str(self.mortality_sensor) + '§' + str(self.external_dropoff) + '§' +\
                          str(self.external_dropoff_controll) + '§' + str(self.external_dropoff_real_time) +\
                          '§' + str(self.external_dropoff_abs_time) + '§' + self.utc_lmt +\
                          '§' + str(self.utc_correction) + '§' + str(self.vhf_beacon_schedule) + '§' + str(self.globalstar) + '§' +\
                          str(self.iridium) + '§' + str(self.iridium_num_of_fixes_gps) +\
                          '§' + str(self.gsm) + '§' + str(self.gsm_vectronic_sim) + '§' +\
                          str(self.gsm_customer_sim_telephone_no) + '§' + str(self.gsm_customer_sim_pin) + '§' +\
                          str(self.gsm_customer_sim_puk) + '§' + str(self.contact_name_airtime_fee) + '§' +\
                          str(self.contact_mail_airtime_fee) + '§' + str(self.notification_mail) + '§' + str(self.notification_sms) +\
                          '§' + str(self.belt_width) + '§' + str(self.belt_thickness) + '§' + str(self.belt_edge) + '§' + str(self.belt_colour) +\
                          '§' + str(self.other_color) + '§' + str(self.belt_labeling) + '§' +\
                          str(self.belt_labeling_instructions) + '§' + str(self.belt_plates) + '§' +\
                          str(self.belt_plates_instructions) + '§' + str(self.cotton_layers) + '§' + str(self.comment) \
                          + '$' + str(self.groundstation_number)
        super(VertexLiteOrderModel, self).save(*args, **kwargs)