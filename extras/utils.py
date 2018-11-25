from collar.models import Staff
from django import forms
from orderContact.forms import InvoiceAddresseForm
from orderContact.forms import DeliveryAddresseForm
from django.conf import settings

PAYMENTOPTIONS = (
    ('Purchase with Order No.', 'Purchase with Order No.'),
    ('Bank Wire Transfer', 'Bank Wire Transfer'),
    ('Check', 'Check'),
    ('Credit Card', 'Credit Card (3.0% service fee)'),
)

BATTERIESIZE = (
    ('', ''),
    ('1C', '1C'),
    ('1D', '1D'),
    ('2D', '2D'),
)

UTCORLMT = (
    ('utc', 'UTC'),
    ('lmt', 'LMT')
)

DROPOFFCONTROLL = (
    ('timeronly', 'Timer controlled'),
    ('TimerAndRadio', 'Timer and Radio controlled')
)

IRIDIUM_CONTRACT_TYPES = (
    ('', ''),
    ('3kByte Plan', '3kByte Plan'),
    ('unlimited plan', 'unlimited plan'),
)

DEFAULTBELTSHAPES = ['round-shaped', 'drop-shaped']
BELTTHICKNESSES = ['3.4 mm (SF/SF)', '4.2 mm (ST/SF)', '5 mm (ST/ST)']
DEFAULTEDGES = ['round', 'smooth']
DEFAULTCOLORS = ['black', 'white', 'tan', 'brown', 'yellow', 'other']
DEFAULTWIDTH = ['25 mm', '32 mm', '38 mm', '50 mm', '63 mm', '75 mm']

BELTSHAPES = ((shape, shape) for shape in DEFAULTBELTSHAPES)

BELTWIDTH = ((width, width) for width in DEFAULTWIDTH)

BELTTHICKNESS = ((thickness, thickness) for thickness in BELTTHICKNESSES)

BELTEDGES = ((edge, edge) for edge in DEFAULTEDGES)

BELTCOLORS = ((color, color) for color in DEFAULTCOLORS)

staffs = Staff.objects.all()
STAFFS = ((staff.initialies, staff.initialies) for staff in staffs)

IRIDIUMMODES = (
    ('3kbyte', '3 kbyte'),
    ('unlimited', 'unlimited')
)

STAFF_EMAIL_ADR = {
    'TT': 'felixeisenmenger@gmx.net',
}

if settings.DEVELOPMENT:
    STAFF_EMAIL_ADR['UT'] = 'test@test.com'

ERROR_CONTEXT = {
            'error': 'Please check your delivery address',
            'invoice_address': InvoiceAddresseForm,
            'delivery_form': DeliveryAddresseForm,
        }

widgets_for_survey_vertex = {
            'animal_species': forms.TextInput(attrs={'title': 'The species of the animal'}),
            'vhf_beacon_frequency': forms.Textarea(attrs={'rows': 2, 'cols': 30}),
            'belt_labeling_instructions': forms.Textarea(attrs={'rows': 4, 'cols': 20, 'style': 'resize:none;',
                                                                'maxlength': 76}),
            'belt_plates_instructions': forms.Textarea(attrs={'rows': 2, 'cols': 20, 'maxlength': 76}),
            'utc_correction': forms.NumberInput(attrs={
                'min': '-13.00', 'max': '13:00', 'step': '0.05', 'autocomplete': 'on',
            }),
            'mortality_sensor': forms.NumberInput(attrs={
                'min': '0', 'max': '140', 'step': '1',
            }),
            'battery_size': forms.HiddenInput(attrs={
                'visibility': 'hidden',
            }),
            'number_of_collars': forms.HiddenInput(attrs={
                'visibility': 'hidden',
            }),
            'nom_collar_circumference': forms.HiddenInput(attrs={
                'visibility': 'hidden',
            }),
            'iridium_num_of_fixes_gps': forms.NumberInput(attrs={
                'min': '0', 'max': '18', 'step': '1',
            }),
            'belt_labeling': forms.CheckboxInput(attrs={
                'class': 'lable_plates', 'onclick': 'lable_function()',
            }),
            'belt_plates': forms.CheckboxInput(attrs={
                'class': 'lable_plates', 'onclick': 'plates_function()',
            }),
            'cotton_layers': forms.NumberInput(attrs={
                'min': '0', 'max': '6', 'step': '1',
            }),
            'iridium_contract_type': forms.Select(choices=IRIDIUM_CONTRACT_TYPES),
            'external_dropoff_real_time': forms.TextInput(attrs={
                'onchange': 'dropOffRealTime()'
            }),
            'external_dropoff_abs_time': forms.TextInput(attrs={
                'onchange': 'dropOffAbsTime()'
            }),
            'globalstar': forms.CheckboxInput(attrs={
                'disabled': True,
            }),
            'iridium': forms.CheckboxInput(attrs={
                'disabled': True,
            }),
        }

labels_for_survey_vertex = {
            'nom_collar_circumference': 'Nominal collar circumference (in cm)',
            'animal_species': '1.1 Animal species',
            'belt_shape': '1.3 Belt shape',
            'belt_width': '1.4 Belt width',
            'belt_thickness': '1.5 Belt thickness',
            'belt_edge': '1.6 Belt edge',
            'belt_colour': '1.7 Belt color',
            'other_color': '',
            'belt_labeling': '1.8 Labelling with contact info',
            'belt_labeling_instructions': 'Label plates',
            'belt_plates': '1.9 Belt markings',
            'belt_plates_instructions': 'Belt markings instructions',
            'reflective_stripes': '1.10 Reflective stripes on belt',
            'vhf_beacon_frequency': '2.1 VHF beacon frequency',
            'mortality_sensor': '2.2 Mortality sensor delay time',
            'notification_mail': 'Notification e-mail',
            'notification_sms': 'Notification SMS (with additional charge)',
            'utc_lmt': '2.3 Timezone',
            'utc_correction': 'UTC correction (h) for schedules',
            'gps_schedule': '2.4 GPS schedule',
            'vhf_beacon_schedule': '2.5 VHF beacon schedule',
            'id_tag': '2.6 ID-Tag option',
            'globalstar': '3.1 GLOBALSTAR',
            'iridium': '3.1 IRIDIUM',
            'iridium_num_of_fixes_gps': 'IRIDIUM number of GPS positions send per message',
            'airtime_contract': 'Upload your airtime fee contract here',
            'contact_name_airtime_fee': 'Airtime fee contact name',
            'contact_mail_airtime_fee': 'Airtime fee contact e-mail',
            'external_dropoff': '4.1 External Drop Off (at extra charge)',
            'external_dropoff_controll': 'External Drop Off controll',
            'external_dropoff_real_time': 'External Drop Off relative release time',
            'external_dropoff_abs_time': 'External Drop Off absolute release time',
            'cotton_layers': '4.2 Amount of cotton spacer (at extra charge)',
            'as_post': 'Invoice via mail',
            'as_email': 'Invoice via e-mail',
            'order_no': 'Purchase Order No.',
            'iridium_contract_type': 'IRIDIUM contract type',
            'owm_gps_schedule': 'Upload your own GPS schedule here',
            'own_vhf_schedule': 'Upload your own VHF schedule here',
        }

help_texte_for_survey_vertex = {
            'belt_shape': 'Round collars are most suitable for '
                          'carnivore while drop shape collars are best fitting for herbivore.',
            'belt_colour': '<b>Note</b>:There is an additional charge for colored belts, <br>'
                           ' <u>black colored belts</u> are free of charge',
            'belt_labeling': '<b>Note:</b> There is an additional charge for label plates',
            'belt_labeling_instructions': 'Please use only max. 4 lines and max. 20 characters per line.',
            'belt_plates': '<b>Note:</b> There is an additional charge for belt markings',
            'belt_plates_instructions': 'Please specify color of marking /vertical or horizontal / and which numbers '
                                        'and/or letters you want.',
            'reflective_stripes': '<b>Note:</b> There is an additional charge for reflective stripes',
            'vhf_beacon_frequency': 'VHF frequencies are possible in the range from 130 MHz – 400 MHz.'
                                    '<br>Most common ranges are between <b>148 MHz – 152 MHz.</b>',
            'mortality_sensor': 'Please choose the period of time in hours without movement until'
                                ' a mortality event should be triggered. <b>Default is 24 hours.</b>',
            'utc_correction': 'If your schedules are programmed in local mean time <b>(LMT)</b>,'
                              ' <br>please specify the <b>UTC correction</b>',
            'gps_schedule': 'Please specify on which times per day a GPS position should be taken, eg. '
                            'every hour or every 13 hours.<br><b>Note:</b> For the Survey collar with <u>GOBALSTAR</u> '
                            'communication are <br><u>only 2 positions per day</u> possible.',
            'vhf_beacon_schedule': 'Please specify the period per day, on which the VHF beacon should be active.',
            'id_tag': 'Can be used for proximity studies. The collar will additionally act as an UHF–ID–Tag. <br>'
                      '<b>Note:</b> There is an additional charge for activating the ID-Tag option on the collar.',
            'globalstar': '<b>Note:</b> For the Survey collar with GOBALSTAR communication are only 2 positions'
                          ' per day possible.',
            'iridium': '<b>Note:</b> For the Survey collar with IRIDIUM communication we recommend'
                       ' 10-12 as max. positions per day to ensure full performance.',
            'iridium_num_of_fixes_gps': 'Recommendation is 4 Fixes per message.',
            'iridium_contract_type': 'The 3kByte Plan is less expensive up to 15 positions per day. For more as 15 positions per day we recommend the unlimited plan.',
            'external_dropoff': 'To retrieve your collar without having to recapture the animal, an external Drop Off'
                                ' can be added to the collar.',
            'external_dropoff_real_time': 'The Drop Off releases the collar at the end of a user-defined time period '
                                          'starting with the removal of the Drop Off magnet. Please state in the '
                                          'format: <b>weeks, days, hours</b>',
            'external_dropoff_abs_time': 'The Drop Off releases the collar at a preprogrammed time and date. '
                                         'Please state in the format: <b>dd.mm.yyyy hh:mm:ss</b>',
            'cotton_layers': 'Works as a rot-off system. The material will decay within time due to environmental '
                             'effects (e.g. rain, sun exposure, humidity, heat) and the behavior of the animal '
                             '(e.g. rub on trees or similar). :  Several layers can be combined to extend the timespan '
                             'but it is impossible to foretell how long it will take to rot off. ',
            'comment': 'Please define here any additional collar specification.',

        }

payment_option_fields = ['payment_option', 'order_no', 'vat_ein_number', 'delivery_time', 'as_post', 'as_email', ]
payment_option_labels = {
            'as_post': 'Invoice as letter per mail',
            'as_email': 'Invoice as letter per e-mail',
            'order_no': 'PO/order number',
            'vat_ein_number': 'VAT or EIN number',
            'delivery_time': 'Latest date of Shipment',
        }
payment_option_widgets = {
            'as_post': forms.CheckboxInput(attrs={
                'onclick': 'viaPost_function()',
                'class': 'emailOrPost',
            }),
            'as_email': forms.CheckboxInput(attrs={
                'onclick': 'viaEmail_function()',
                'class': 'emailOrPost',
            }),
        }
payment_option_help_texts = {
            'delivery_time': 'A delivery time before this prefilled date will be confirmed by our Sales department'
        }