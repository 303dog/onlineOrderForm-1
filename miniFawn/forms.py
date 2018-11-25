from django import forms
import datetime

from django.forms import BaseFormSet
from extras.utils import payment_option_fields
from extras.utils import  payment_option_labels
from extras.utils import payment_option_widgets
from extras.utils import payment_option_help_texts
from miniFawn.models import MiniFawnOrderModel

from extras.utils import labels_for_survey_vertex
from extras.utils import widgets_for_survey_vertex
from extras.utils import help_texte_for_survey_vertex


class MiniFawnCreateForm(forms.ModelForm):
    class Meta:
        model = MiniFawnOrderModel
        fields = ['animal_species', 'vhf_beacon_frequency', 'mortality_sensor',
                  'notification_mail', 'notification_sms', 'utc_lmt', 'utc_correction', 'gps_schedule',
                  'owm_gps_schedule', 'skip_count', 'vhf_beacon_schedule', 'own_vhf_schedule', 'id_tag', 'globalstar',
                  'contact_mail_airtime_fee', 'airtime_contract', 'cotton_layers', 'comment',
                  'battery_size', 'number_of_collars', ]

        widgets_for_miniFawn = widgets_for_survey_vertex
        widgets_for_miniFawn.update({
            'cotton_layers': forms.NumberInput(attrs={
                'min': '0', 'max': '2', 'step': '1',
            }),
        })

        labels_for_miniFawn = labels_for_survey_vertex
        labels_for_miniFawn.update({
            'skip_count': '2.5 Skip count',
            'vhf_beacon_schedule': '2.6 VHF beacon schedule',
            'id_tag': '2.7 ID-Tag option',
        })

        widgets = widgets_for_miniFawn
        labels = labels_for_miniFawn
        help_texts = help_texte_for_survey_vertex

    def clean(self):
        cleaned_data = super(MiniFawnCreateForm, self).clean()
        order_no = cleaned_data.get('order_no')
        utc_lmt = cleaned_data.get('utc_lmt')
        utc_correction = cleaned_data.get('utc_correction')
        cotton_layers = cleaned_data.get('cotton_layers')
        vhf_beacon_frequency = cleaned_data.get('vhf_beacon_frequency')
        animal_species = cleaned_data.get('animal_species')
        globalstar = cleaned_data.get('globalstar')
        as_email = cleaned_data.get('as_email')
        as_post = cleaned_data.get('as_post')
        invoice_mail = cleaned_data.get('invoice_mail')

        if as_email is True and as_post is True:
            self.add_error('as_email', 'Please choose via mail OR via e-mail')
            self.add_error('as_post', 'Please choose via mail OR via e-mail')

        if as_email is False and as_post is False:
            self.add_error('as_email', 'Please choose via mail OR via e-mail')
            self.add_error('as_post', 'Please choose via mail OR via e-mail')

        if as_email is True and invoice_mail is None:
            self.add_error('invoice_mail', 'Please fill in the invoice e-mail address')

        if len(vhf_beacon_frequency) < 2:
            self.add_error('vhf_beacon_frequency', 'Please add your VHF Beacon Frequency')

        if utc_lmt != 'lmt' and utc_lmt != 'utc':
            self.add_error('utc_lmt', 'Please select a Timezone')
        elif utc_lmt == 'lmt' and utc_correction is None:
            self.add_error('utc_correction', 'Please specify the UTC correction')

        if cotton_layers is not None and cotton_layers > 6:
            self.add_error('cotton_layers', 'Cotton layers cannot be higher than 6')


class MFArticleForm(forms.ModelForm):
    class Meta:
        model = MiniFawnOrderModel
        fields = ['number_of_collars', 'min_belt_circumference', 'max_belt_circumference']
        widgets = {
            'number_of_collars': forms.NumberInput(attrs={
                'min': '0', 'max': '99', 'step': '1',
            }),
            'min_belt_circumference': forms.NumberInput(attrs={
                'min': '0', 'max': '99', 'step': '1', 'class': 'long_num_input'
            }),
            'max_belt_circumference': forms.NumberInput(attrs={
                'min': '0', 'max': '99', 'step': '1', 'class': 'long_num_input'
            })
        }

    def clean(self):
        cleaned_data = super(MFArticleForm, self).clean()
        min_collar_circumference = cleaned_data.get('min_belt_circumference')
        number_of_collars = cleaned_data.get('number_of_collars')
        if min_collar_circumference is None:
            self.add_error('min_belt_circumference', 'Please select a min collar circumference')

        if number_of_collars is None:
            self.add_error('number_of_collars', 'Please select a quantity of collar')


class MFPaymentOptionForm(forms.ModelForm):
    class Meta:
        model = MiniFawnOrderModel
        fields = payment_option_fields
        labels = payment_option_labels
        widgets = payment_option_widgets
        help_texts = payment_option_help_texts


class MFBaseArticleForm(BaseFormSet):
    def clean(self):
        cleaned_data = super(MFBaseArticleForm, self).clean()
        #
        # for form in self.forms:
        #     if form['min_belt_circumference'] is None:
        #         self.add_error('min_belt_circumference', 'Select a size')