import datetime
from django import forms
from django.forms import BaseFormSet
from extras.utils import BATTERIESIZE
from extras.utils import labels_for_survey_vertex
from extras.utils import help_texte_for_survey_vertex
from extras.utils import widgets_for_survey_vertex
from extras.utils import payment_option_fields
from extras.utils import  payment_option_labels
from extras.utils import payment_option_widgets
from extras.utils import payment_option_help_texts
from .models import SurveyOrderModel


class SurveyCreateForm(forms.ModelForm):
    class Meta:
        model = SurveyOrderModel
        fields = ['animal_species', 'belt_shape', 'belt_width',
                  'belt_thickness', 'belt_edge', 'belt_colour', 'other_color', 'belt_labeling', 'belt_labeling_instructions',
                  'belt_plates', 'belt_plates_instructions', 'reflective_stripes',
                  'vhf_beacon_frequency', 'mortality_sensor', 'notification_mail', 'notification_sms', 'utc_lmt',
                  'utc_correction', 'gps_schedule', 'owm_gps_schedule', 'vhf_beacon_schedule', 'own_vhf_schedule', 'id_tag',
                  'globalstar', 'iridium', 'iridium_num_of_fixes_gps', 'iridium_contract_type',
                  'contact_name_airtime_fee', 'contact_mail_airtime_fee', 'airtime_contract', 'external_dropoff',
                  'external_dropoff_controll', 'external_dropoff_real_time', 'external_dropoff_abs_time',
                  'cotton_layers', 'comment', 'battery_size', 'number_of_collars', 'nom_collar_circumference', ]

        # exclude = ['contacts_faktura_id', 'delivery_addresse', 'created_at', 'order_acceptet',
        #            'same_addr', 'customer_invoice_address', 'customer_staff', 'operation_Number']
        widgets = widgets_for_survey_vertex
        labels = labels_for_survey_vertex
        help_texts = help_texte_for_survey_vertex

    def clean(self):
        cleaned_data = super(SurveyCreateForm, self).clean()
        belt_shape = cleaned_data.get('belt_shape')
        belt_thickness = cleaned_data.get('belt_thickness')
        belt_width = cleaned_data.get('belt_width')
        external_drop_off = cleaned_data.get('external_dropoff')
        utc_lmt = cleaned_data.get('utc_lmt')
        utc_correction = cleaned_data.get('utc_correction')
        belt_labeling_plates = cleaned_data.get('belt_labeling_plates')
        belting_instructions = cleaned_data.get('belting_instructions')
        cotton_layers = cleaned_data.get('cotton_layers')
        vhf_beacon_frequency = cleaned_data.get('vhf_beacon_frequency')
        animal_species = cleaned_data.get('animal_species')
        globalstar = cleaned_data.get('globalstar')
        iridium = cleaned_data.get('iridium')
        belt_color = cleaned_data.get('belt_colour')
        other_color = cleaned_data.get('other_color')
        external_dropoff = cleaned_data.get('external_dropoff')
        external_dropoff_real_time = cleaned_data.get('external_dropoff_real_time')
        external_dropoff_abs_time = cleaned_data.get('external_dropoff_abs_time')

        if belt_width is None:
            self.add_error('belt_width', 'Please choose a belt witdh')

        if belt_thickness is None:
            self.add_error('belt_thickness', 'Please choose a belt thickness')

        if animal_species is None:
            self.add_error('animal_species', 'Please tell us for which animal the collars are')

        if belt_shape is None:
            self.add_error('belt_shape', 'Please choose a belt shape')

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

        if globalstar is False and iridium is False:
            self.add_error('globalstar', 'Choose globalstar or iridium')
            self.add_error('iridium', 'Choose globalstar or iridium')
        if globalstar is True and iridium is True:
            self.add_error('globalstar', 'Choose globalstar or iridium')
            self.add_error('iridium', 'Choose globalstar or iridium')

        if len(vhf_beacon_frequency) < 2:
            self.add_error('vhf_beacon_frequency', 'Please add your VHF Beacon Frequency')

        # if vhf_beacon_frequency is not None:
        #     if ';' not in vhf_beacon_frequency:
        #         self.add_error('vhf_beacon_frequency', 'Please split your VHF Beacon Frequencies by a semicolon')

        if utc_lmt != 'lmt' and utc_lmt != 'utc':
            self.add_error('utc_lmt', 'Please select a Timezone')
        elif utc_lmt == 'lmt' and utc_correction is None:
            self.add_error('utc_correction', 'Please specify the UTC correction')

        if belt_labeling_plates is not None and len(belt_labeling_plates) > 1 and belting_instructions is None:
            print(belt_labeling_plates)
            self.add_error('belting_instructions', 'Don\'t miss to give us instructions for your belting')

        if cotton_layers is not None and cotton_layers > 6:
            self.add_error('cotton_layers', 'Cotton layers cannot be higher than 6')
        if belt_color is not None:
            if belt_color == 'Other' and other_color is None:
                self.add_error('other_color', 'Please tell us your Color')

        if external_dropoff is not None:
            if external_dropoff_abs_time is not None and external_dropoff_real_time is not None:
                if len(external_dropoff_abs_time) > 1 and len(external_dropoff_real_time) > 1:
                    self.add_error('external_dropoff_real_time', 'Please choose relative release time OR'
                                                             ' absolute release time')
                    self.add_error('external_dropoff_abs_time', 'Please choose relative release time OR '
                                                            'absolute release time')


class ArticleForm(forms.ModelForm):
    class Meta:
        model = SurveyOrderModel
        fields = ['battery_size', 'number_of_collars', 'nom_collar_circumference']
        widgets = {
            'battery_size': forms.Select(
                choices=BATTERIESIZE
            ),
            'number_of_collars': forms.NumberInput(attrs={
                'min': '0', 'max': '99', 'step': '1',
            }),
            'nom_collar_circumference': forms.TextInput(attrs={
                'rows': 1, 'cols': 20,
            })
        }

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        battery_size = cleaned_data.get('battery_size')
        number_of_collars = cleaned_data.get('number_of_collars')
        if battery_size is None:
            self.add_error('battery_size', 'Please select a batterysize')

        if number_of_collars is None or number_of_collars < '1':
            self.add_error('battery_size', 'Please select a batterysize')


class BaseArticleForm(BaseFormSet):
    def clean(self):
        cleaned_data = super(BaseArticleForm, self).clean()

        for form in self.forms:
            if form['battery_size'] is None:
                self.add_error('battery_size', 'Select a size')


class PaymentOptionForm(forms.ModelForm):
    class Meta:
        model = SurveyOrderModel
        fields = payment_option_fields
        labels = payment_option_labels
        widgets = payment_option_widgets
        help_texts = payment_option_help_texts