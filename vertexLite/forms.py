import datetime

from django import forms
from vertexLite.models import VertexLiteOrderModel
from extras.utils import help_texte_for_survey_vertex
from extras.utils import labels_for_survey_vertex
from extras.utils import widgets_for_survey_vertex
from extras.utils import payment_option_fields
from extras.utils import  payment_option_labels
from extras.utils import payment_option_widgets
from extras.utils import payment_option_help_texts

ALLBATTERIESIZE = (
    ('', ''),
    ('1C', '1C'),
    ('1D', '1D'),
    ('2D', '2D'),
    ('3D', '3D'),
    ('4D', '4D'),
    ('5D', '5D'),
    ('6D', '6D'),
    ('7D', '7D'),
)


class VertexLiteCreateForm(forms.ModelForm):
    class Meta:
        model = VertexLiteOrderModel
        fields = ['animal_species', 'belt_shape', 'belt_width', 'belt_thickness', 'belt_edge', 'belt_colour',
                  'other_color', 'belt_labeling', 'belt_labeling_instructions', 'belt_plates',
                  'belt_plates_instructions', 'reflective_stripes', 'vhf_beacon_frequency', 'mortality_sensor',
                  'notification_mail', 'notification_sms', 'utc_lmt', 'utc_correction', 'gps_schedule',
                  'owm_gps_schedule', 'vhf_beacon_schedule', 'own_vhf_schedule', 'id_tag', 'globalstar', 'iridium',
                  'iridium_num_of_fixes_gps', 'iridium_contract_type', 'gsm', 'gsm_vectronic_sim', 'groundstation_number',
                  'gsm_customer_sim_telephone_no', 'gsm_customer_sim_pin', 'gsm_customer_sim_puk', 'store_on_board',
                  'contact_name_airtime_fee', 'contact_mail_airtime_fee', 'airtime_contract', 'internal_dropoff',
                  'internal_dropoff_controll', 'internal_dropoff_real_time', 'internal_dropoff_abs_time', 'external_dropoff',
                  'external_dropoff_controll', 'external_dropoff_real_time', 'external_dropoff_abs_time',
                  'cotton_layers', 'comment', 'battery_size', 'number_of_collars', 'nom_collar_circumference', ]

        labels_for_vertexLite = labels_for_survey_vertex
        labels_for_vertexLite.update({
            'gsm': '3.1 GSM',
            'store_on_board': '3.1 Store on board',
            'internal_dropoff': '4.1 Internal Drop Off',
            'internal_dropoff_controll': 'Internal Drop Off controll',
            'internal_dropoff_real_time': 'Internal Drop Off relative release time',
            'internal_dropoff_abs_time': 'Internal Drop Off absolute release time',
        })
        labels_for_vertexLite['external_dropoff'] = '4.2 External Drop Off (at extra charge)'
        labels_for_vertexLite['cotton_layers'] = '4.3 Amount of cotton spacer (at extra charge)'

        widgets_for_vertexLite = widgets_for_survey_vertex
        widgets_for_vertexLite.update({
            'internal_dropoff_real_time': forms.TextInput(attrs={
                'onchange': 'internalDropOffRealTime()',
            }),
            'internal_dropoff_abs_time': forms.TextInput(attrs={
                'onchange': 'internalDropOffAbsTime()',
            }),
            'gsm': forms.CheckboxInput(attrs={
                'disabled': True,
            }),
            'store_on_board': forms.CheckboxInput(attrs={
                'disabled': True,
            })
        })

        widgets = widgets_for_vertexLite
        labels = labels_for_vertexLite
        help_texts = help_texte_for_survey_vertex

    def clean(self):
        cleaned_data = super(VertexLiteCreateForm, self).clean()
        belt_shape = cleaned_data.get('belt_shape')
        belt_thickness = cleaned_data.get('belt_thickness')
        belt_width = cleaned_data.get('belt_width')
        belt_edge = cleaned_data.get('belt_edge')
        internal_drop_off = cleaned_data.get('internal_dropoff')
        internal_dropoff_real_time = cleaned_data.get('internal_dropoff_real_time')
        internal_dropoff_abs_time = cleaned_data.get('internal_dropoff_abs_time')
        external_drop_off = cleaned_data.get('external_dropoff')
        external_dropoff_real_time = cleaned_data.get('external_dropoff_real_time')
        external_dropoff_abs_time = cleaned_data.get('external_dropoff_abs_time')
        utc_lmt = cleaned_data.get('utc_lmt')
        utc_correction = cleaned_data.get('utc_correction')
        battery_size = cleaned_data.get('battery_size')
        belt_labeling_plates = cleaned_data.get('belt_labeling_plates')
        belting_instructions = cleaned_data.get('belting_instructions')
        cotton_layers = cleaned_data.get('cotton_layers')
        vhf_beacon_frequency = cleaned_data.get('vhf_beacon_frequency')
        animal_species = cleaned_data.get('animal_species')
        globalstar = cleaned_data.get('globalstar')
        iridium = cleaned_data.get('iridium')
        store_on_board = cleaned_data.get('store_on_board')
        belt_color = cleaned_data.get('belt_colour')
        other_color = cleaned_data.get('other_color')
        as_email = cleaned_data.get('as_email')
        as_post = cleaned_data.get('as_post')
        invoice_mail = cleaned_data.get('invoice_mail')
        gsm = cleaned_data.get('gsm')

        if as_email is True and as_post is True:
            self.add_error('as_email', 'Please choose via mail OR via e-mail')
            self.add_error('as_post', 'Please choose via mail OR via e-mail')

        if as_email is False and as_post is False:
            self.add_error('as_email', 'Please choose via mail OR via e-mail')
            self.add_error('as_post', 'Please choose via mail OR via e-mail')

        if as_email is True and invoice_mail is None:
            self.add_error('invoice_mail', 'Please fill in the invoice e-mail address')

        if belt_width is None:
            self.add_error('belt_width', 'Please choose a belt witdh')

        if belt_thickness is None:
            self.add_error('belt_thickness', 'Please choose a belt thickness')

        if belt_edge is None:
            self.add_error('belt_edge', 'Please choose a belt edge')

        if battery_size is not None and belt_width is not None:
            if '1C' not in battery_size and float(belt_width.split()[0]) < 38.0:
                self.add_error('belt_width', 'For this belt width you must pick another battery size')

        if animal_species is None:
            self.add_error('animal_species', 'Please tell us for which animal the collars are')

        if belt_shape is None:
            self.add_error('belt_shape', 'Please choose a belt shape')
        # if belt_width is not None and belt_thickness is not None:
        #     if belt_thickness.name == 'SF/SF' and belt_width.width < 63:
        #         pass
        #     else:
        #         self.add_error('belt_thickness', 'Choose a lower thickness or change belt-width')
        #         self.add_error('belt_width', 'Please change your belt-thickness')
        if internal_drop_off is not None:
            if internal_drop_off:
                if internal_dropoff_abs_time is not None and internal_dropoff_real_time is not None:
                    if (len(internal_dropoff_abs_time) > 2) and (len(internal_dropoff_real_time) > 2):
                        self.add_error('external_dropoff_abs_time', 'Please choose only one option')
                        self.add_error('external_dropoff_real_time', 'Please choose only one option')
                elif internal_dropoff_abs_time is None and internal_dropoff_real_time is None:
                    self.add_error('external_dropoff_abs_time', 'Please choose one')
                    self.add_error('external_dropoff_real_time', 'Please choose one')
                elif internal_dropoff_abs_time is not None:
                    try:
                        datetime.datetime.strptime(external_dropoff_abs_time, '%d.%m.%Y %H:%M:%S')
                    except:
                        self.add_error('external_dropoff_abs_time', 'Please adhere to the given format: dd.mm.yyyy hh:mm:ss')

        if external_drop_off is not None:
            if external_drop_off:
                if external_dropoff_abs_time is not None and external_dropoff_real_time is not None:
                    if (len(external_dropoff_abs_time) > 2) and (len(external_dropoff_real_time) > 2):
                        self.add_error('external_dropoff_abs_time', 'Please choose only one option')
                        self.add_error('external_dropoff_real_time', 'Please choose only one option')
                elif external_dropoff_abs_time is None and external_dropoff_real_time is None:
                    self.add_error('external_dropoff_abs_time', 'Please choose one')
                    self.add_error('external_dropoff_real_time', 'Please choose one')
                elif external_dropoff_abs_time is not None:
                    try:
                        datetime.datetime.strptime(external_dropoff_abs_time, '%d.%m.%Y %H:%M:%S')
                    except:
                        self.add_error('external_dropoff_abs_time', 'Please adhere to the given format: dd.mm.yyyy hh:mm:ss')

        # if globalstar is False and iridium is False and gsm is False:
        #     self.add_error('globalstar', 'Choose globalstar or iridium')
        #     self.add_error('iridium', 'Choose globalstar or iridium')

        if len(vhf_beacon_frequency) < 2:
            self.add_error('vhf_beacon_frequency', 'Please add your VHF Beacon Frequency')

        if utc_lmt != 'lmt' and utc_lmt != 'utc':
            self.add_error('utc_lmt', 'Please select a Timezone')
        elif utc_lmt == 'lmt' and utc_correction is None:
            self.add_error('utc_correction', 'Please specify the UTC correction')

        if belt_labeling_plates is not None and len(belt_labeling_plates) > 1 and belting_instructions is None:
            self.add_error('belting_instructions', 'Don\t miss to give us instructions for your belting')

        if cotton_layers is not None and cotton_layers > 6:
            self.add_error('cotton_layers', 'Cotton layers cannot be higher than 6')
        if belt_color is not None:
            if belt_color == 'Other' and other_color is None:
                self.add_error('other_color', 'Please tell us your Color')
            if belt_color == '' and other_color is None:
                self.add_error('belt_colour', 'Please tell us your Color')


class VLArticleForm(forms.ModelForm):
    class Meta:
        model = VertexLiteOrderModel
        fields = ['battery_size', 'number_of_collars', 'nom_collar_circumference']
        widgets = {
            'battery_size': forms.Select(
                choices=ALLBATTERIESIZE
            ),
            'number_of_collars': forms.NumberInput(attrs={
                'min': '0', 'max': '99', 'step': '1', 'onchange': 'changeToTable()',
            }),
            'nom_collar_circumference': forms.TextInput(attrs={
                'rows': 1, 'cols': 20,
            })
        }

    def clean(self):
        cleaned_data = super(VLArticleForm, self).clean()
        battery_size = cleaned_data.get('battery_size')
        number_of_collars = cleaned_data.get('number_of_collars')
        if battery_size is None:
            self.add_error('battery_size', 'Please select a batterysize')

        if number_of_collars is None:
            self.add_error('battery_size', 'Please select a batterysize')


class VLPaymentOptionForm(forms.ModelForm):
    class Meta:
        model = VertexLiteOrderModel
        fields = payment_option_fields
        labels = payment_option_labels
        widgets = payment_option_widgets
        help_texts = payment_option_help_texts