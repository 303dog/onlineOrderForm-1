from django import forms
from traptransmitter.models import TrapTransmitterOrderModel
from extras.utils import widgets_for_survey_vertex
from extras.utils import labels_for_survey_vertex
from extras.utils import help_texte_for_survey_vertex
from extras.utils import payment_option_fields
from extras.utils import payment_option_labels
from extras.utils import payment_option_widgets
from extras.utils import payment_option_help_texts


class TrapTransmitterCreateForm(forms.ModelForm):
    class Meta:
        model = TrapTransmitterOrderModel
        fields = ['number_of_collars', 'globalstar', 'iridium', 'vhf_beacon_schedule', 'contact_name_airtime_fee',
                  'contact_mail_airtime_fee', 'notification_mail', 'notification_sms', 'vhf_beacon_frequency',
                  'world_location', 'interval', 'comment']

        widgets_for_trapTransmitter = widgets_for_survey_vertex
        widgets_for_trapTransmitter.update({
            'interval': forms.NumberInput(attrs={
                'min': '1', 'max': '48', 'step': '1',
            }),
        })
        widgets_for_trapTransmitter['number_of_collars'] = forms.NumberInput(attrs={
                'min': '1', 'max': '48', 'step': '1',
            })

        labels_for_trapTransmitter = labels_for_survey_vertex
        labels_for_trapTransmitter.update({
            'interval': '3.3 Interval in which the status message should be send (1h - 48h)',
            'world_location': '3.2 Please indicate whether the Trap Transmitter will be used',
            'number_of_collars': '1.1 Number of TT3 Trap Transmitter'
        })

        labels_for_trapTransmitter['globalstar'] = '2.1 Globalstar'
        labels_for_trapTransmitter['iridium'] = '2.1 Iridium'
        labels_for_trapTransmitter['vhf_beacon_schedule'] = '2.2 VHF beacon schedule'
        labels_for_trapTransmitter['vhf_beacon_frequency'] = '3.1 VHF beacon frequency'

        help_texte_for_trapTransmitter = help_texte_for_survey_vertex
        help_texte_for_trapTransmitter.update({
            'interval': 'Note: We donot reccomend to send more as 4 status messages per day - so avoid intervalls from 1-5 hours.'
        })

        help_texte_for_trapTransmitter['globalstar'] = ''
        help_texte_for_trapTransmitter['iridium'] = ''

        widgets = widgets_for_trapTransmitter
        labels = labels_for_trapTransmitter
        help_texts = help_texte_for_trapTransmitter

    def clean(self):
        cleaned_data = super(TrapTransmitterCreateForm, self).clean()
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


class TTPaymentOptionForm(forms.ModelForm):
    class Meta:
        model = TrapTransmitterOrderModel
        fields = payment_option_fields
        labels = payment_option_labels
        widgets = payment_option_widgets
        help_texts = payment_option_help_texts